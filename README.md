# Jacob's Jinja Too

A simple wrapper around Jinja2 templatung with a collection of custom filters.

## Installation

```sh
pip3 install jacobs-jinja-Too
```

## Example Usage

```python
from jacobsjinjatoo import Templator as jj2

t = jj2.MarkdownTemplator()
t.add_template_dir('templates/')
params = {
    "name": "My Name"
}
t.render_template('foo.jinja2', output_name='foo.txt', **params)
```

## License 

GPLv2
