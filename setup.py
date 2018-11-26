# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Wallet',
    version='0.1.0',
    description='Wallet for BuyWithTokens.org',
    long_description=readme,
    author='Arnon Hongklay',
    author_email='arnon@hongklay.com',
    url='https://github.com/arnonhongklay/wallet',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
