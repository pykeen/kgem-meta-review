import os

import yaml

HERE = os.path.abspath(os.path.dirname(__file__))
BENCHMARKS_PATH = os.path.join(HERE, '_data', 'benchmarks.yml')
SURVEYS_PATH = os.path.join(HERE, '_data', 'surveys.yml')


def _sort(path):
    with open(path) as file:
        data = yaml.safe_load(file)
    data = sorted(data, key=lambda x: x['year'])
    with open(path, 'w') as file:
        yaml.safe_dump(data, file)


def main():
    _sort(BENCHMARKS_PATH)
    _sort(SURVEYS_PATH)


if __name__ == '__main__':
    main()
