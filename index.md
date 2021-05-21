---
layout: home
---
This page contains a list of knowledge graph embedding model (KGEM) surveys and
benchmarking studies. It's generated with GitHub
Pages from <a href="https://github.com/pykeen/kgem-meta-review"><img alt="GitHub logo"
src="img/github-icon.svg" width="16" height="16" /> pykeen/kgem-meta-review</a>. Content on this site
is available under the [CC0 1.0 Universal](https://github.com/pykeen/kgem-meta-review/blob/main/LICENSE)
license.

## Contributing

You can contribute to this list in one of the following ways:

1. [Add a benchmark](https://github.com/pykeen/kgem-meta-review/edit/main/_data/benchmarks.yml) through the GitHub editor
2. [Add a survey](https://github.com/pykeen/kgem-meta-review/edit/main/_data/surveys.yml) through the GitHub editor

## Benchmark Studies

{% for entry in site.data.benchmarks %}
<strong><a href="{{ entry.link }}">{{ entry.title }}</a></strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
<br />
{% if entry contains "arxiv" %}[![arXiv](https://img.shields.io/badge/arXiv-{{ entry.arxiv }}-b31b1b)](https://arxiv.org/abs/{{ entry.arxiv }}){% endif %} {% if entry contains "github" %}[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github | replace: "-", ""}}-black?logo=github)](https://github.com/{{ entry.github }}){% endif %} {% if entry contains "models" %}![Models](https://img.shields.io/badge/Models-{{ entry.models.size }}-blue){% endif %} {% if entry contains "datasets" %}![Datasets](https://img.shields.io/badge/Datasets-{{ entry.datasets.size }}-blueviolet){% endif %}
{% if entry contains "comment" %}<p>{{ entry.comment }}</p>{% endif %}
{% endfor %}

## Surveys

{% for entry in site.data.surveys %}
<strong><a href="{{ entry.link }}">{{ entry.title }}</a></strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
{% if entry contains "arxiv" %}<br />[![arXiv](https://img.shields.io/badge/arXiv-{{ entry.arxiv }}-b31b1b)](https://arxiv.org/abs/{{ entry.arxiv }}){% endif %} {% if entry contains "github" %}[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github | replace: "-", ""}}-black?logo=github)](https://github.com/{{ entry.github }}){% endif %} {% if entry contains "models" %}![Models](https://img.shields.io/badge/Models-{{ entry.models.size }}-blue){% endif %} {% if entry contains "datasets" %}![Datasets](https://img.shields.io/badge/Datasets-{{ entry.datasets.size }}-blueviolet){% endif %}
{% if entry contains "comment" %}<p>{{ entry.comment }}</p>{% endif %}
{% endfor %}
