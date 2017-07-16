#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 20:55
# @Author  : Shijun Gong
# @Version    : 0.1.0
# @File    : setup.py
# @Software: PyCharm

from distutils.core import setup
import py2exe
import sys
sys.argv.append('py2exe')

setup(
    version = "0.1.0",
    description = "Auto Connect Internet",
    name = "GSJ_AC",
    console = [{"script":'login.py'}],
)