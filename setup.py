#!/usr/bin/env python
# -*-* coing: UTF-8 -*-

from setuptools import setup

setup(
    name='Visual Check',
    version='1',
    packages=['Visual Check'],
    url='www.zagangsum.com',
    license='GNU General Public License',
    author='gareth.cripps',
    author_email='gareth.cripps@zagangsum.com',
    description='Production line visual standards',
    platforms='any',
    install_requires=[
        'pillow', 'APscheduler',
    ]
)
