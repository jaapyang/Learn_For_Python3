#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle
import math


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


if __name__ == '__main__':
    bob = turtle.Turtle()
    polygon(bob, 360, 1)
    bob.pu()

    # wait for the user to close the window
    turtle.mainloop()
