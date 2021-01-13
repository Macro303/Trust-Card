#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='Trust Card',
    version='1.1.0',
    long_description=open('README.md').read(),
    license='MIT',
    author='Macro303',
    author_email='',
    url='https://github.com/Macro303/Trust-Card',
    packages=find_packages(exclude=('test',)),
    install_requires=['pyyaml == 5.3.1', 'colorama == 0.4.3', 'PyInstaller == 4.2']
)
