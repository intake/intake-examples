#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='intake_example_package',
    version='0.0.1',
    description='Demonstrated entrypoint method for data installation',
    py_modules=['intake_example_package'],
    packages=find_packages(),
    package_data={'': ['*.yaml']},
    include_package_data=True,
    install_requires=['intake'],
    zip_safe=False,
    entry_points={
        'intake.catalogs': [
            'sea = intake_example_package:cat'
        ]
    }
)
