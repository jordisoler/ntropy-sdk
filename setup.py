#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["requests", "tqdm", "typing"]

setup_requirements = []

test_requirements = []

setup(
    author="David Buchmann",
    author_email="david@ntropy.network",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="SDK for the Ntropy API",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="ntropy_sdk",
    name="ntropy_sdk",
    packages=find_packages(include=["ntropy_sdk", "ntropy_sdk.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/ntropy-network/ntropy-sdk",
    version="2.0.1",
    zip_safe=False,
)
