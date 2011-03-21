#! /usr/bin/env python
# vi:ts=4:et

from setuptools import *

import os, sys
import distutils
from distutils.core import setup
from distutils.extension import Extension
from distutils.util import split_quoted

def get_kw(**kw): return kw

setup_args = get_kw(
    name="pseudo-python-lzo",
    version="0.1",
    description="Python interface for lzop",
    author="Yamashita Yuu",
    author_email="yamashita@geishatokyo.com",
    url="https://github.com/yyuu/pseudo-python-lzo/",
    licence="GNU General Public License (GPL)",
    long_description="""
This module provides interface for lzop(1) like python-lzo.

LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and *very* fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.""",
)

##print distutils.__version__
if distutils.__version__ >= "1.0.2":
    setup_args["platforms"] = "All"

apply(setup, (), setup_args)

