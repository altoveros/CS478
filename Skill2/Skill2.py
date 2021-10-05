# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:44:34 2021

@author: ialto
"""

import turtle


t = turtle.Turtle()
t.pensize(5)


for i in range(5):
    t.forward(80)
    t.right(144)
    t.forward(80)
    t.left(72)
    
t.penup()
t.goto(-24.72,-147)
t.pendown()
t.color('red')
t.circle(115)
t.done()
