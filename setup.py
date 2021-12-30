# -*- coding: utf-8 -*-
import codecs
import os
from setuptools import setup

from comver import __app_name__, __version__

here = os.path.dirname(os.path.abspath(__file__))

with open('README.md') as f:
    readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

# Requirements
with codecs.open(os.path.join(here, 'requirements.txt')) as f:
    install_requirements = [
        line.split('#')[0].strip() for line in f.readlines() if not line.startswith('#')
    ]

setup(
    name=__app_name__,
    version=__version__,
    description='bla bla bla',
    long_description=readme,
    license=license,
    install_requires=install_requirements,
    py_modules=['comver'],
    entry_points='''
        [console_scripts]
        comver=comver.main:cli
    ''',
)
