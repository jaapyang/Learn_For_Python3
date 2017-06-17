#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""test for oop_basic.Person"""
import unittest

from oop_basic.Person import Person

__author__ = 'Paul yang'


class TestFor_Person(unittest.TestCase):
    def test_Init_singleParameter_setValueForName_success(self):
        p = Person('paul')
        self.assertEqual(p.name, 'paul')

    def test_init_more_parameter_input_success(self):
        p = Person('paul', 30)
        self.assertEqual(p.name, 'paul')
        self.assertEqual(p.age, 30)

    def test_sayHellow_success(self):
        p = Person('Lisa')
        actual = p.sayHellow()
        expected = r'Hi,I\'m %s,how are you?' % 'Lisa'
        self.assertEqual(actual, expected)

    def test_setAge_inputValueIs10_success(self):
        p = Person('paul')
        p.set_Age(10)
        self.assertEqual(p.age,10)

    def test_setAge_inputValueIsLessThan0_throwExpectedException(self):
        try:
            p = Person('paul')
            p.set_Age(-10)
        except AttributeError as e:
            self.assertIsNotNone(e)

    def test_setAge_inputValueIsLargeThan200_throwExpectedException(self):
        try:
            p = Person('paul')
            p.set_Age(310)
        except AttributeError as e:
            self.assertIsNotNone(e)

if __name__ == '__main__':
    unittest.main()
