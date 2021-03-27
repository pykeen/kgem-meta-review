# -*- coding: utf-8 -*-

"""Update the vocabulary.json file with anything that's been manually curated."""

import json
import os

import yaml

from constants import BENCHMARKS_PATH, SURVEY_PATH, VOCABULARY_PATH, load_curation


def main():
    if not os.path.exists(VOCABULARY_PATH):
        vocabulary = {"models": {}, "datasets": {}}
    else:
        with open(VOCABULARY_PATH) as file:
            vocabulary = json.load(file)

    model_vocabulary = vocabulary['models']

    for path in (BENCHMARKS_PATH, SURVEY_PATH):
        with open(path) as file:
            data = yaml.safe_load(file)
        for entry in data:
            for model in entry.get('models', []):
                model_vocabulary.setdefault(model, [])

    for entry in load_curation()['novel']:
        if model := entry.get('model'):
            if isinstance(model, str):
                model = [model]
            for m in model:
                model_vocabulary.setdefault(m, [])

    with open(VOCABULARY_PATH, 'w') as file:
        json.dump(vocabulary, file, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
