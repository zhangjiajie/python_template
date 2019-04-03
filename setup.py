#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="",
    version="0.0.1",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    tests_require=[],
    author="Jiajie Zhang",
    author_email="",
    description="",
    keywords="",
    url="",
    zip_safe=True,
    include_package_data=True,
    package_data={
        '': ['*.dat', '*.gctx'],
    }
)
