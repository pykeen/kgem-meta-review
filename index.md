---
layout: home
---
This page contains a list of benchmarking papers on the link prediction task using knowledge graph
embedding models.

{% for entry in site.data.papers %}
<strong><a href="{{ entry.link }}">{{ entry.title }}</a></strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
<br />
{% if entry contains "arxiv" %}[![arXiv](https://img.shields.io/badge/arXiv-{{ entry.arxiv }}-b31b1b)](https://arxiv.org/abs/{{ entry.arxiv }}){% endif %}
{% if entry contains "github" %}![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github }}-black?logo=github){% endif %}
![Models](https://img.shields.io/badge/Models-{{ entry.models.size }}-blue)
![Datasets](https://img.shields.io/badge/Datasets-{{ entry.datasets.size }}-blueviolet)
{% endfor %}
