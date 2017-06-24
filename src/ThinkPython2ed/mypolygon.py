#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle
import math

""" test for my private commit
    test for contribution when I commit in the default branch
"""

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = float(360 / n)
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    print(arc_length)
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


if __name__ == '__main__':
    bob = turtle.Turtle()
    arc(bob, 100, 360)

    # wait for the user to close the window
    turtle.mainloop()
