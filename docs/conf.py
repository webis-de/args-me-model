import sys
from pathlib import Path

project = 'args-me-model'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinxcontrib.autodoc_pydantic'
]

autosummary_generate = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html'
    ]
}

sys.path.insert(0, str(Path('..', 'src').resolve()))
