"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


A simple implementation of the turtle drawing robot using the stddraw module.
See Program 3.2.4 in the text for a similar, well-documented implementation.
"""

import stddraw
import math

class Turtle:

    def __init__(self, x, y):
        """
        :param x: initial x position
        :param y: initial y position
        """
        self._x = x
        self._y = y
        self._angle = 0.0 # face left to begin

    def turn_left(self, radians):
        self._angle += radians

    def go_forward(self, step):
        dx = step * math.cos(self._angle)
        dy = step * math.sin(self._angle)
        # leave a line first
        stddraw.line(self._x, self._y, self._x + dx, self._y + dy)
        # actually move my turtle
        self._x += dx
        self._y += dy

if __name__ == '__main__':
    # test code
    pass
