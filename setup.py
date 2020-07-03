#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import io
from setuptools import setup, find_packages

with io.open("README.rst", encoding="utf-8") as readme_file, io.open(
    "HISTORY.rst", encoding="utf-8"
) as history_file:
    long_description = readme_file.read() + "\n\n" + history_file.read()

install_requires = [
    "click>=6.0",
]

setup_requires = [
    "pytest-runner",
    # TODO(starofrainnight): put setup requirements (distutils extensions, etc.) here
]

tests_requires = [
    "pytest",
    # TODO: put package test requirements here
]

setup(
    name="ahk-bin",
    version="0.0.4",
    description="A python package that bundled with workable AutoHotkey binary which could works for 'ahk' package ",
    long_description=long_description,
    author="Hong-She Liang",
    author_email="starofrainnight@gmail.com",
    url="https://github.com/starofrainnight/ahk-bin",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license="GNU General Public License v2 (GPLv2)",
    zip_safe=False,
    keywords="ahkbin,ahk-bin",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    tests_require=tests_requires,
    data_files=[('Scripts', ['ahkbin\\ahk\\AutoHotkey.exe'])],
    setup_requires=setup_requires,
)
