# -*- coding: utf-8 -*-

"""Constants for the autoreviewer."""

import json
import os
from functools import partial

import pystow
import yaml

HERE = os.path.abspath(os.path.dirname(__file__))

# Local resources
VOCABULARY_PATH = os.path.join(HERE, 'vocabulary.json')
RESULTS = os.path.join(HERE, 'results.json')

DATA_PATH = os.path.abspath(os.path.join(HERE, os.pardir, '_data'))
SURVEY_PATH = os.path.join(DATA_PATH, 'surveys.yml')
BENCHMARKS_PATH = os.path.join(DATA_PATH, 'benchmarks.yml')
CURATION_PATH = os.path.join(DATA_PATH, 'curation.yml')

# Cached resources
MOD = pystow.module('pykeen', 'metareview')
PAPERS_PATH = MOD.join(name='papers.json')


# Loaders

def _load_yaml(path):
    with open(path) as file:
        return yaml.safe_load(file)


def _load_json(path):
    with open(path) as file:
        return json.load(file)


load_survey = partial(_load_yaml, SURVEY_PATH)
load_benchmarks = partial(_load_yaml, BENCHMARKS_PATH)
load_curation = partial(_load_yaml, CURATION_PATH)
load_vocabulary = partial(_load_json, VOCABULARY_PATH)
