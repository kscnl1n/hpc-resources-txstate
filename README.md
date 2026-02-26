# HPC Resources Portal

Sphinx documentation (Alabaster theme) for the HPC Resources Portal.

## Build

```bash
pip install -r requirements-docs.txt
sphinx-build -b html docs docs/_build
```

Open `docs/_build/index.html`. On Read the Docs, connect the repo and it will build from `docs/conf.py`.

## Optional images

Add under `docs/images/` for inline figures: `1.jpg`, `2.png`, `3.jpg`, `4.png`, `5.jpg`, `6.png`. Build succeeds without them (with warnings).
