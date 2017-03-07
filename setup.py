#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from mode import __author__, __version__, __license__
 
setup(
        name             = 'mode',
        version          = __version__,
        description      = '',
        license          = __license__,
        author           = __author__,
        author_email     = '',
        url              = 'https://github.com/pachicourse/mode-py.git',
        keywords         = 'MODE Device pip github python',
        packages         = find_packages(),
        install_requires = [],
)
