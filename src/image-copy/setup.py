#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from codecs import open
from setuptools import find_packages, setup

VERSION = "1.0.3"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = []

setup(
    name='image-copy-extension',
    version=VERSION,
    description='Support for copying managed vm images between regions',
    long_description='Support for copying managed vm images between regions',
    license='MIT',
    author='Tamir Kamara',
    author_email='tamir.kamara@microsoft.com',
    url='https://github.com/Azure/azure-cli-extensions/tree/main/src/image-copy',
    classifiers=CLASSIFIERS,
    package_data={'azext_imagecopy': ['azext_metadata.json']},
    packages=find_packages(),
    install_requires=DEPENDENCIES
)
