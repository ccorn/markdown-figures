#!/usr/bin/env python

from distutils.core import setup

long_description = \
"""Extension for Python-Markdown to parse figure elements, optionally with a caption.
"""

setup(name='mdx_figures',
      description='Figures extension for Python-Markdown',
      long_description=long_description,
      author='Helder Correia',
      author_email='me@heldercorreia.com',
      version='0.1',
      url='https://github.com/helderco/markdown-figures',
      py_modules=['mdx_figures'])
