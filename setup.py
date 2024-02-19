# -*- coding: utf-8 -*-
import os

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

from setuptools import find_packages, setup

README = '''
This is an implementation of [GCRA](https://en.wikipedia.org/wiki/Generic_cell_rate_algorithm) for rate limiting based on Redis.

The code requires Redis version 3.2 or newer since it relies on [replicate_commands](https://redis.io/commands/eval/#replicating-commands-instead-of-scripts) feature.
'''

setup(
    name='pyredis_rate_limiter',
    version='1.0.0',
    description='A Redis-backed rate limiting based on GCRA implementation in Python',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Adam Zhou',
    author_email='adamzhouisnothing@gmail.com',
    url='https://github.com/amazingchow/redlock-py',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "jsonschema==4.21.1",
        "loguru==0.7.2",
        "redis==5.0.1"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': []
    }
)
