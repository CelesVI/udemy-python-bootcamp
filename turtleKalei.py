import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','blue','green','yellow','orange','grey','purple','pink'])

def circle(size,angle,forw):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(forw)
    circle(size,angle+5,forw+3)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(60,40,1)


t.hideturtle()

