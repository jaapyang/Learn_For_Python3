#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.score = score
        self.name = name

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"


bart = Student("Bart Simpson", 90)
lisa = Student("Lisa Simpson", 30)

bart.print_score()
lisa.print_score()
print(lisa.get_grade())
