#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://pythonhosted.org/an_example_pypi_project/setuptools.html
# also see http://peterdowns.com/posts/first-time-with-pypi.html

import os
from setuptools import setup

#utility function to read the readme file
# here = os.path.dirname(os.path.abspath(__file__))
# try:
# 	with open(os.path.join(here,'README.md')) as doc:
# 		long_desc = doc.read()
# except:
# 	long_desc = ''

# Install requests==2.5.3 to avoid InsecurePlatformWarning message

setup(
	name='restcountries_py',
	version='v0.1',
	author='Darshan Adhikari',
	author_email='dsn.adh@hotmail.com',
	description='A Python wrapper for Restcountries API provided by https://restcountries.eu',
	keywords=['countries', 'rest countries', 'wrapper', 'database', 'api'],
	url='https://github.com/99darshan/restcountries_py',
	download_url='https://github.com/99darshan/restcountries_py/tarball/v0.1',
	packages=['restcountries_py'],
	#long_description=long_desc,
	install_requires=['requests'],
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Topic :: Utilities",
		"License :: OSI Approved :: MIT License",
	],
)
