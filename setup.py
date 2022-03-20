# -*- coding: utf-8 -*-
import codecs
import os
from setuptools import setup

from comver import __app_name__, __version__


here = os.path.dirname(os.path.abspath(__file__))

with open('README.md') as f:
    readme = f.read()

# with open('LICENSE') as f:
    # license = f.read()

def get_requirements(file_name: str) -> str:
    with codecs.open(os.path.join(here, file_name)) as f:
        return [
            line.split('#')[0].strip() for line in f.readlines() if not line.startswith('#')
        ]   

setup(
    name=__app_name__,
    version=__version__,
    description='comver description',
    long_description=readme,
    install_requires=get_requirements('requirements.txt'),
    extras_require={
        'test': get_requirements('test-requirements.txt')
    },
    py_modules=['comver'],
    entry_points='''
        [console_scripts]
        comver=comver.main:cli
    ''',
)
