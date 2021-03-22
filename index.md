---
layout: home
---
This page contains a list of knowledge graph embedding model (KGEM) link prediction
benchmarking studies. You can contribute to this list
[here](https://github.com/pykeen/kgembmr/edit/main/_data/papers.yml).

{% for entry in site.data.papers %}
<strong><a href="{{ entry.link }}">{{ entry.title }}</a></strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
<br />
{% if entry contains "arxiv" %}[![arXiv](https://img.shields.io/badge/arXiv-{{ entry.arxiv }}-b31b1b)](https://arxiv.org/abs/{{ entry.arxiv }}){% endif %}
{% if entry contains "github" %}[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github | replace: "-", ""}}-black?logo=github)](https://github.com/{{ entry.github }}){% endif %}
{% if entry contains "models" %}![Models](https://img.shields.io/badge/Models-{{ entry.models.size }}-blue){% endif %}
{% if entry contains "datasets" %}![Datasets](https://img.shields.io/badge/Datasets-{{ entry.datasets.size }}-blueviolet){% endif %}
{% endfor %}
