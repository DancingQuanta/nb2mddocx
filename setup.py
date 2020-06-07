#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='nb2mddocx',
      version='0.0.1',
      description='Microsoft word friendly markdown exporter for Jupyter Notebook',
      author='Andrew Tolmie',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      install_requires=['traitlets', 'jupyter'],
        entry_points = {
            'nbconvert.exporters': [
                'mddocx = nb2mddocx:MdDocxExporter',
            ],
        }
     )
