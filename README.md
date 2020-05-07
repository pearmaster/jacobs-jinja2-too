# Jacob's Jinja Too

A simple wrapper around Jinja2 templating with a collection of custom filters.  [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) is a templating language for Python.

Only tested with Python3.7.

The main purpose for this project is for depencency management as this diagram shows:

```plantuml
[Top Level Project] --> [jacobs-jinja-too] : uses
[Top Level Project] --> [Another Project]  : depends
[Another Project] --> [jacobs-jinja-too]   : uses
```

## Installation

```sh
pip3 install jacobs-jinja-too
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
