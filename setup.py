#!/usr/bin/env python
'''
setup.py - Python distutils setup file for PyGCSUDP package.

Copyright (C) 2014 Simon D. Levy

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this code. If not, see <http://www.gnu.org/licenses/>.
'''

from distutils.core import setup
setup (name = 'PyGCSUDP',
version = '0.1',
description = 'OpenPilot GCS UDP control utility',
packages = ['gcsudp'],
author='Simon D. Levy',
author_email='simon.d.levy@gmail.com',
url='https://github.com/simondlevy/PyGCSUD'P,
license='LGPL',
platforms='Linux; Windows',
install_requires = ['PyGame']
)
