#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pymodbus",
    version="2.0",
    packages=find_packages(exclude=['examples', 'test']),
    exclude_package_data={'': ['examples', 'test', 'tools', 'doc']},
)
