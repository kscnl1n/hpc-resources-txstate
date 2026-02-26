# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'HPC Resources Portal'
copyright = '2025'
author = ''
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# Alabaster theme options (optional)
html_theme_options = {
    'description': 'High-Performance Computing resources and programs',
    'github_user': '',
    'github_repo': '',
    'fixed_sidebar': True,
    'sidebar_collapse': False,
}

# -- Options for HTML output (Read the Docs) ---------------------------------
# ReadTheDocs uses the theme from conf.py; Alabaster is built-in.
