#! ENV/Scripts/python

from setuptools import setup, find_packages

setup(
	name='Trust Card',
	version='0.0.0',
	long_description=open('README.md').read(),
	license='GPL-3.0',
	author='Macro303',
	author_email='',
	url='https://github.com/Macro303/Trust-Card',
	packages=find_packages(exclude=('test',)),
	install_requires=['pyyaml >= 4.0.0']
)
