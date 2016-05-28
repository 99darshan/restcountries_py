# -*- coding: utf-8 -*-

# http://pythonhosted.org/an_example_pypi_project/setuptools.html
# also see http://peterdowns.com/posts/first-time-with-pypi.html

import os
from distutils.core import setup

# utility function to read the readme file
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Install requests==2.5.3 to avoid InsecurePlatformWarning message

setup(
	name='restcountries',
	version='0.1',
	author='Darshan Adhikari',
	author_email='dsn.adh@hotmail.com',
	description='A Python wrapper for Restcountries API provided by restcountries.eu',
	keywords=['countries', 'rest countries', 'wrapper', 'database', 'api'],
	url='https://github.com/99darshan/restcountries-py',
	download_url='https://github.com/99darshan/restcountries/tarball/0.1',
	packages=['restcountries'],
	long_description=read('README.md'),
	install_requires=['requests==2.5.3'],
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
