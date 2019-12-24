#!/usr/bin/env python
"""yiss netconf client library"""
import setuptools


__author__ = "Carl Montanari"

with open("README.md", "r") as f:
    README = f.read()

setuptools.setup(
    name="yiss",
    version="2019.12.24",
    author=__author__,
    author_email="carl.r.montanari@gmail.com",
    description="Netconf client for network devices built on ncclient",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/carlmontanari/wtfy",
    packages=setuptools.find_packages(),
    install_requires=["ncclient>=0.6.6", "lxml>=4.4.2", "xmltodict>=0.12.0"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)
