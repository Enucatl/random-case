from setuptools import setup

setup(
    name = "randomcase",
    version = "0",
    scripts = [
        'randomcase.py',
    ],

    install_requires = [
        'click',
    ],

    # metadata for upload to PyPI
    author = "Matteo Abis",
    description = "convert case to random case",
    license = "GNU GPL 3",
    keywords = "case converter",
    # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)
