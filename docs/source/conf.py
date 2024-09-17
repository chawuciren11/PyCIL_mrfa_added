# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PyCIL'
copyright = 'xx,xxx'
author = 'CLLab-NJU'

release = '1.0'
version = '1.0.2'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
    'recommonmark',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'searchbox.html'],
}
# -- Options for EPUB output
epub_show_urls = 'footnote'

import os
import sys
from os.path import dirname, abspath

sys.path.insert(0, abspath('..'))
root_dir = dirname(dirname(abspath(__file__)))