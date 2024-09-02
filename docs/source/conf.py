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
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # 用于“上一页”和“下一页”链接
        'searchbox.html',  # 包含搜索框
        'donate.html',  # 可以是自定义的侧边栏模板
    ]
}
# -- Options for EPUB output
epub_show_urls = 'footnote'
