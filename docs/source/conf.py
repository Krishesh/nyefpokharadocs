# Configuration file for the Sphinx documentation builder.
import sys
import os
import re

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath(__file__))
# -- Project information

project = 'NYEF Pokhara'
copyright = '2022, nyefpokhara'
author = 'Krishesh shrestha'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']


templates_path = ['_templates']
source_suffix = '.rst'
# -- Options for HTML output
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static/']

# -- Options for EPUB output
epub_show_urls = 'footnote'
html_context = {}

html_show_sourcelink = True
