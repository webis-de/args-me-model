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
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html'
    ]
}

src_path = Path('..', 'src').resolve()
sys.path.insert(0, str(src_path))
with open(str(src_path / "args_me_model" / "__init__.py")) as file:
    for line in file:
        if line.startswith("__version__"):
            version = line.split('"')[1]

rst_epilog = """
.. _code: https://github.com/webis-de/args-me-model/tree/v{0}/"
.. _package: https://pypi.org/project/args-me-model/{0}/"
""".format(version)
