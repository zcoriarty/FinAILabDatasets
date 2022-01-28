import sys, os

sys.path.insert(0, os.path.abspath('extensions'))

extensions = [
	# "nbsphinx"
	'sphinx_tabs.tabs',
	'sphinx_panels'
	# 'hoverxref.extension',
]

html_theme = 'press'

# hoverxref_tooltip_maxwidth = 650
# hoverxref_auto_ref = True

# hoverxref_sphinxtabs = True
# hoverxref_mathjax = True



sphinx_tabs_valid_builders = ['readthedocshtml']

panels_add_bootstrap_css = False

# sphinx_tabs_valid_builders = ['linkcheck']

source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = 'index'

extensions = [
    'sphinx.ext.autosectionlabel'
]
autosectionlabel_prefix_document = True

# exclude_patterns = [
# 	'_build'
# ]
# nbsphinx_allow_errors = True
# learn how to make a theme
