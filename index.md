---
layout: home
---
This page contains a list of benchmarking papers on the link prediction task using knowledge graph
embedding models.

{% for entry in site.data.papers %}
<strong><a href="{{ entry.link }}">{{ entry.title }}</a></strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
<br />
{% if entry contains "arxiv" %}
<a href="https://arxiv.org/abs/{{ entry.arxiv }}">
<img style="display: inline" src="https://img.shields.io/badge/arXiv-{{ entry.arxiv }}-b31b1b" />
</a>
{% endif %}
{% if entry contains "github" %}
<a href="https://github.com/{{ entry.github }}">
<img style="display: inline" src="https://img.shields.io/badge/GitHub-{{ entry.github }}-black?logo=github" />
</a>
{% endif %}
<img style="display: inline" src="https://img.shields.io/badge/Models-{{ entry.models.size }}-blue" />
<img style="display: inline" src="https://img.shields.io/badge/Datasets-{{ entry.datasets.size }}-blueviolet" />
{% endfor %}
