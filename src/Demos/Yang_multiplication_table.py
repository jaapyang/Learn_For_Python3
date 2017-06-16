#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Learn for IO commands"""


# 九九乘法表

def Yang_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{} X {} = {}\t'.format(j, i, i * j), end='')
        print()


if __name__ == '__main__':
    Yang_multiplication_table()
