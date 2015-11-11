#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


HERE = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def make_readme(root_path):
    FILES = ('README.rst', 'LICENSE', 'CHANGELOG', 'CONTRIBUTORS')
    for filename in FILES:
        filepath = os.path.realpath(os.path.join(root_path, filename))
        if os.path.isfile(filepath):
            with open(filepath, mode='r') as f:
                yield f.read()


LONG_DESCRIPTION = "\r\n\r\n----\r\n\r\n".join(make_readme(HERE))


setup(
    name='django-storagecellar',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=(
        'Django>=1.7',
    ),
    tests_require=(
        'pytest>=2.6.4',
        'pytest-cov>=1.8.1',
        'pytest-django>=2.8.0',
    ),
    cmdclass={'test': PyTest},
    author='Keryn Knight',
    author_email='python-package@kerynknight.com',
    description="",
    long_description=LONG_DESCRIPTION,
    keywords=[],
    include_package_data=True,
    url='https://github.com/kezabelle/django-storagecellar',
    download_url='https://github.com/kezabelle/django-storagecellar',
    zip_safe=False,
    license="BSD License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
    ],
)
