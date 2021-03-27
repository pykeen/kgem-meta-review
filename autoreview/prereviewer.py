# -*- coding: utf-8 -*-

"""Pre-review script for arXiv."""

import itertools as itt
import json
import os
import tarfile
from collections import Counter
from functools import lru_cache
from operator import itemgetter
from typing import List, Mapping

import yaml
from tqdm import tqdm

from constants import BENCHMARKS_PATH, MOD, PAPERS_PATH, RESULTS, SURVEY_PATH, VOCABULARY_PATH, load_curation

SKIP_PREFIXES = [
    'astro-ph',
    'cond-mat',
    'gr-qc',
    'hep-ph',
    'math',
    'nucl-th',
    'physics',
]


def main(include_pre: bool = False):
    curation_data = load_curation()
    skip_arxiv_ids = set(curation_data['skip'])

    if not include_pre:
        for entry in itt.chain.from_iterable(curation_data[key] for key in ('novel', 'irrelevant', 'hits')):
            skip_arxiv_ids.add(entry['arxiv'].strip())

    it = tqdm(iter_papers(include_pre=include_pre), desc='Potential reviews')
    results = []
    for arxiv_id, data in it:
        if arxiv_id in skip_arxiv_ids:
            continue
        it.set_postfix({'arxiv': arxiv_id})
        try:
            counter, ci_counter = check(arxiv_id)
        except UnicodeError:
            tqdm.write(f'unicode error on {arxiv_id}')
            continue
        except tarfile.ReadError:
            tqdm.write(f'tar error on {arxiv_id}')
            continue
        except FileNotFoundError:
            tqdm.write(f'file not found error on {arxiv_id}')
            continue
        if len(counter) < 3:  # If at least 2 models aren't mentioned, skip it
            continue
        # tqdm.write(tabulate(counter.most_common(), headers=['token', f'{arxiv_id}_count']))
        results.append({
            'arxiv': arxiv_id,
            'counts': dict(counter),
            # 'case_insensitive_counts': dict(ci_counter),
            **data,
        })

    # Put papers with highest number of hits from the CV first in the curation sheet
    results = sorted(results, key=itemgetter('arxiv'))
    with open(RESULTS, 'w') as file:
        json.dump(results, file, sort_keys=True, indent=2)


@lru_cache(maxsize=1)
def get_vocabulary() -> Mapping[str, List[str]]:
    with open(VOCABULARY_PATH) as file:
        return json.load(file)


def iter_papers(include_pre: bool = False):
    rv = dict()
    surveys = dict(_get_pre_curated_papers(SURVEY_PATH))
    benchmarks = dict(_get_pre_curated_papers(BENCHMARKS_PATH))
    if include_pre:
        rv.update(surveys)
        rv.update(benchmarks)
    for arxiv_id, entry in _get_queued_papers():
        if arxiv_id not in surveys and arxiv_id not in benchmarks:
            rv[arxiv_id] = entry
    return sorted(rv.items())


def _get_pre_curated_papers(path: str):
    with open(path) as file:
        entries = yaml.safe_load(file)
    for entry in entries:
        if arxiv_id := entry.pop('arxiv', None):
            yield str(arxiv_id), entry


def _get_queued_papers():
    with open(PAPERS_PATH) as file:
        data = json.load(file)
    yield from data.items()


def check(arxiv_id: str):
    download_path = MOD.ensure(name=f'{arxiv_id}.tar.gz', url=f'https://arxiv.org/e-print/{arxiv_id}')
    extract_directory = MOD.join(arxiv_id)
    with tarfile.open(download_path) as tar:
        tar.extractall(path=extract_directory)

    counter = Counter()
    ci_counter = Counter()
    for directory, _, names in os.walk(extract_directory):
        for name in names:
            if not name.endswith('.tex'):
                continue
            with open(os.path.join(directory, name)) as file:
                text = file.read()
                for token, synonyms in get_vocabulary().items():
                    if (
                        token in text
                        or token.capitalize() in text
                        or (synonyms and any(synonym in text for synonym in synonyms))
                    ):
                        counter[token] += 1
                    if token.casefold() in text.casefold():
                        ci_counter[token] += 1
    return counter, ci_counter


if __name__ == '__main__':
    main()
