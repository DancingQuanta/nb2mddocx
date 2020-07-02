{% extends 'markdown.tpl' %}

{% macro get_label(cell) -%}
	{% if cell.metadata.label: -%}
{{ "{" }}#{{ cell.metadata.label }}{{ "}" }}
	{% else -%}
	{% endif -%}
{%- endmacro %}

{% macro figure_link(cell, path) -%}
![{{ cell.metadata.get('caption', '') }}]({{ path }}){{ get_label(cell) }}
{%- endmacro %}

{% macro table_caption(cell) -%}
: {{ cell.metadata.get('caption', '') }} {{ get_label(cell) }}
{%- endmacro %}

{% block data_svg %}
{{ figure_link(cell, output.metadata.filenames['image/svg+xml']) }}
{% endblock data_svg %}

{% block data_png %}
{{ figure_link(cell, output.metadata.filenames['image/png']) }}
{% endblock data_png %}

{% block data_jpg %}
{{ figure_link(cell, output.metadata.filenames['image/jpeg']) }}
{% endblock data_jpg %}

{% block data_html %}
{% endblock data_html %}

{% block data_markdown %}
{{ output.data['text/markdown'] }}

{%- if cell.metadata.caption: %}
: {{ cell.metadata.get('caption', '') }} {{ get_label(cell) }}
{% endif -%}
{% endblock data_markdown %}

% Disable input cells
{% block input scoped %}
{%- if nb.metadata.remove_code: %}
{%- else -%}
```python
{{cell.source}}
```
{% endif -%}
{% endblock input %}

% Exlude error output
{% block error %}
{% endblock error %}
