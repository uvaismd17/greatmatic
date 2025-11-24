# conf.py - minimal advanced config for Sphinx + MyST
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = "My Docs Blog"
author = "Ydainel"
release = "0.1"

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# MyST (Markdown) extensions
myst_enable_extensions = [
    "colon_fence",
    "attrs_block",
    "attrs_inline",
]

# Optional: show source link
html_show_sourcelink = True