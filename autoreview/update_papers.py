# -*- coding: utf-8 -*-

"""Download arXiv papers from a defined list of queries."""

import json
import os
from xml.etree import ElementTree

import requests

from constants import PAPERS_PATH

URL = 'https://export.arxiv.org/api/query?search_query='
ATOM = '{http://www.w3.org/2005/Atom}'

QUERIES = [
    'graph+embedding+survey',
    'graph+embedding+benchmark',
    'graph+embedding+benchmarking',
    'graph+embedding+review',
    'link+prediction+review',
    'link+prediction+survey',
    'link+prediction+benchmark',
    'link+prediction+benchmarking',
]


def search(query):
    url = URL + query + '&max_results=100'
    res = requests.get(url)
    tree = ElementTree.fromstring(res.content)
    rv = {}
    for entry in tree.findall(f'{ATOM}entry'):
        arxiv_id = entry.find(f'{ATOM}id').text[len('http://arxiv.org/abs/'):].rsplit('v', 1)[0]
        entry = {
            'title': entry.find(f'{ATOM}title').text.strip().replace('\n', ' '),
            'published': entry.find(f'{ATOM}published').text.strip().replace('\n', ' '),
            'summary': entry.find(f'{ATOM}summary').text.strip().replace('\n', ' '),
        }
        rv[arxiv_id] = entry
    return rv


def main():
    if not os.path.exists(PAPERS_PATH):
        papers = {}
    else:
        with open(PAPERS_PATH) as file:
            papers = json.load(file)

    for query in QUERIES:
        papers.update(search(query))

    with open(PAPERS_PATH, 'w') as file:
        json.dump(papers, file, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
