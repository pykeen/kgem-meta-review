import json
import os
import tarfile
from collections import Counter
from functools import lru_cache
from typing import Any, Mapping, Set

import pystow
import yaml
from tabulate import tabulate
from tqdm import tqdm

HERE = os.path.abspath(os.path.dirname(__file__))
MODELS_PATH = os.path.join(HERE, 'vocabulary.json')
PAPERS_PATH = os.path.join(HERE, 'papers.txt')
RESULTS = os.path.join(HERE, 'results.json')

DATA_PATH = os.path.abspath(os.path.join(HERE, os.pardir, '_data'))
SURVEY_PATH = os.path.join(DATA_PATH, 'surveys.yml')
BENCHMARKS_PATH = os.path.join(DATA_PATH, 'benchmarks.yml')

MOD = pystow.module('pykeen', 'metareview')


def main():
    it = tqdm(sorted(get_papers().items()))
    results = []
    for arxiv_id, data in it:
        it.set_postfix({'arxiv': arxiv_id})
        counter = check(arxiv_id)
        tqdm.write(tabulate(counter.most_common(), headers=['token', f'{arxiv_id}_count']))
        results.append({
            'arxiv_id': arxiv_id,
            'counts': dict(counter),
            **data,
        })
    with open(RESULTS, 'w') as file:
        json.dump(results, file, sort_keys=True, indent=2)


@lru_cache(maxsize=1)
def get_vocabulary() -> Set[str]:
    with open(MODELS_PATH) as file:
        return set(json.load(file))


def get_papers() -> Mapping[str, str]:
    return {
        **_get_pre_curated_papers(SURVEY_PATH),
        **_get_pre_curated_papers(BENCHMARKS_PATH),
        **_get_queued_papers(),
    }


def _get_pre_curated_papers(path: str) -> Mapping[str, Any]:
    with open(path) as file:
        x = yaml.safe_load(file)
    return {
        str(arxiv): entry
        for entry in x
        if (arxiv := entry.pop('arxiv', None))
    }


def _get_queued_papers() -> Mapping[str, Any]:
    with open(PAPERS_PATH) as file:
        return {
            line.strip(): {}
            for line in file
        }


def check(arxiv_id: str):
    download_path = MOD.ensure(name=f'{arxiv_id}.tar.gz', url=f'https://arxiv.org/e-print/{arxiv_id}')
    extract_directory = MOD.join(arxiv_id)
    with tarfile.open(download_path) as tar:
        tar.extractall(path=extract_directory)

    counter = Counter()
    for directory, _, names in os.walk(extract_directory):
        for name in names:
            if not name.endswith('.tex'):
                continue
            with open(os.path.join(directory, name)) as file:
                text = file.read()
                for token in get_vocabulary():
                    if token in text:
                        counter[token] += 1
    return counter


if __name__ == '__main__':
    main()
