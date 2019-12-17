from setuptools import setup

setup(
    name='pre-commit-populate-pylint-requirements',
    version='1.0',
    install_requires=[
        'ruamel.yaml',
    ],
    scripts=['pre-commit-populate-pylint-requirements'])
