#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='intake_example_package',
    version='0.0.1',
    description='Demonstrates entrypoint method for data installation',
    packages=find_packages(),
    package_data={'': ['*.yaml']},
    include_package_data=True,
    install_requires=['intake>=0.5.5'],
    zip_safe=False,
    entry_points={
        'intake.catalogs': [
            'sea_cat = intake_example_package:cat',
            'sea_data = intake_example_package:data'
        ]
    }
)
