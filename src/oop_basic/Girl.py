#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Paul yang'


class girl(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def breast(self, size):
        self.breast = size

    def color(self, color):
        print('%s is %s' % (self.name, color))

    def how(self):
        print('%s breast is %s' % (self.name,self.breast))

if __name__ == '__main__':
    canglaoshi = girl('canglaoshi')
    canglaoshi.breast(90)
    canglaoshi.color('white')
    canglaoshi.how()