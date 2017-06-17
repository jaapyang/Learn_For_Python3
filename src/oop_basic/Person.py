#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Paul yang'


# 定义一个类Person
class Person(object):
    # 构造函数
    def __init__(self, name, age: object = 18):
        self.name = name
        self.age = age

    # 定义一个属性，用于给age赋值，并检验值的正确性，不正确时抛出异常

    def set_Age(self, value):
        if 0 >= value >= 200:
            raise AttributeError('the value has out of range')
        else:
            self.__setattr__('age',value)

    # 定义一个方法，并在测试中调用它
    def sayHellow(self):
        return r'Hi,I\'m %s,how are you?' % self.name
