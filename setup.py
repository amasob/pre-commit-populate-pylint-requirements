from setuptools import setup

setup(
    name='pre-commit-populate-pylint-requirements',
    version='1.0.1',
    install_requires=[
        'ruamel.yaml',
    ],
    py_modules=['pre_commit_populate_pylint_requirements'],
    scripts=['pre_commit_populate_pylint_requirements.py'],
    entry_points={'console_scripts': ['pre-commit-populate-pylint-requirements=pre_commit_populate_pylint_requirements:main']},
)
