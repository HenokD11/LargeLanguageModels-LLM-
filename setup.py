#!/usr/bin/env python
"""Setup script for the py-pip-install-test package."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pytest==7.1.0']

test_requirements = ['pandas', 'matplotlib', 'sklearn',
                     'flask', 'cohere', 'pytest>=3', ]

setup(
    author="Henok",
    email="henokd1@gmail.com",
    python_requires='>=3.6',
    description="Large Language Models",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='Large Language model, gpt-3, deep_learning, unit_testing, pytest',
    name='Large-LanguageModels-LLM-',
    packages=find_packages(include=['src', 'src.*']),
    test_suite='Tests',
    tests_require=test_requirements,
    url='https://github.com/HenokD11/LargeLanguageModels-LLM-',
    version='0.1.0',
    zip_safe=False,
)