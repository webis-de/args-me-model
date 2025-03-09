# args-me-model development notes

- Running unittests (automatically on push)
  ```shell
  PYTHONPATH=src python3 -m unittest
  ```

- Running linter (automatically on push)
  ```shell
  pip install flake8
  flake8 src --count --max-complexity=10 --max-line-length=127 --statistics
  ```

- Building documentation (automatically on release)
  ```shell
  pip install -r docs/requirements
  sphinx-build -b html docs/ docs/_build
  ```

- Release new version
    - Change `__version__` in [`__init__.py`](../src/args_me_model/__init__.py)
    - Add a release via [Github web interface](https://github.com/webis-de/args-me-model/releases/new), tagged `v<VERSION>`
