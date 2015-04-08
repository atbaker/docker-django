# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django-example
version = django-example.__version__

setup(
    name='django_example',
    version=version,
    author='',
    author_email='andrew.tork.baker@gmail.com',
    packages=[
        'django-example',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['django-example/manage.py'],
)