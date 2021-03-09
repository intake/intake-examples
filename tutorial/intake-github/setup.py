#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='intake-github',
    version='0.0.1',
    description='Tutorial plugin: github issues',
    url='',
    maintainer='Trainee',
    maintainer_email='',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['intake', 'pygithub'],
    long_description="",
    entry_points={
        'intake.drivers': [
            'github_issues = intake_github:GithubIssuesSource',
        ]
    },
    zip_safe=False,
)
