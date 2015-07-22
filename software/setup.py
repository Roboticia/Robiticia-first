#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages


def version():
    with open('poppy_dof4_arm_mini/_version.py') as f:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='poppy-dof4-arm-mini',
      version=version(),
      packages=find_packages(),

      install_requires=['pypot >= 2.2', 'poppy-creature'],

      setup_requires=['setuptools_git >= 0.3', ],

      include_package_data=True,
      exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=False,

      author='Pierre Rouanet, Jonathan Grizou, Matthieu Lapeyre',
      author_email='pierre.rouanet@gmail.com',
      description=' Poppy 4 dof arm mini Software Library',
      url='https://github.com/poppy-project/poppy-4dof-arm-mini',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      **extra
      )
