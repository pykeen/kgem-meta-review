---
layout: home
---
This page contains a list of knowledge graph embedding model (KGEM) surveys and
benchmarking studies. You can contribute to this list by
[adding a benchmark](https://github.com/pykeen/kgembmr/edit/main/_data/benchmarks.yml) or
[adding a survey](https://github.com/pykeen/kgembmr/edit/main/_data/surveys.yml) through
the GitHub editor or by forking the repository and sending a pull request.

## Benchmark Studies

{% for entry in site.data.benchmarks %}
<strong><a href="{{ entry.link }}">{{ entry.title }}</a></strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
<br />
{% if entry contains "arxiv" %}[![arXiv](https://img.shields.io/badge/arXiv-{{ entry.arxiv }}-b31b1b)](https://arxiv.org/abs/{{ entry.arxiv }}){% endif %}
{% if entry contains "github" %}[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github | replace: "-", ""}}-black?logo=github)](https://github.com/{{ entry.github }}){% endif %}
{% if entry contains "models" %}![Models](https://img.shields.io/badge/Models-{{ entry.models.size }}-blue){% endif %}
{% if entry contains "datasets" %}![Datasets](https://img.shields.io/badge/Datasets-{{ entry.datasets.size }}-blueviolet){% endif %}
{% endfor %}

## Surveys

{% for entry in site.data.surveys %}
<strong><a href="{{ entry.link }}">{{ entry.title }}</a></strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
{% if entry contains "arxiv" %}<br />[![arXiv](https://img.shields.io/badge/arXiv-{{ entry.arxiv }}-b31b1b)](https://arxiv.org/abs/{{ entry.arxiv }}){% endif %}
{% endfor %}
