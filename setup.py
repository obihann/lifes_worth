#!/usr/bin/env python

from worth.worth import Main
from distutils.core import setup

setup(
    packages=['worth'],
    package_dir={'worth': 'worth'},
    name='worth',
    version=Main.version,
    description='Caculate your lifes worth',
    author='Jeff Hann',
    author_email='jeffhann@gmail.com',
    url='https://github.com/obihann/lifes-worth',
    license='GNU General Public License v2',
    classifiers=[
        'Environment :: Console'
    ],
)
