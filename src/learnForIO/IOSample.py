#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Learn for IO commands"""
__author__ = 'Paul yang'


def __getPath():
    return r'D:/io.txt'


with open(__getPath(), 'w') as f:
    f.write('hello world!')
    print('write to successful')

with open(__getPath(), 'r') as f:
    print(f.read())

with open(__getPath(), 'rb') as f:
    print('read as binary:')
    print(f.read())
