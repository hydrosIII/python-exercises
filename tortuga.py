import tkinter
import turtle
import math
import random

m=turtle.Turtle()


m.clear()
m.speed(0)

def angulorandom():
    while True:
        x =random.randint(1,60)
        y = 360.0/x
        if (y).is_integer() is True:
                             break
    return x



a=int(angulorandom())

def numeroveces ():
    y = a
    x = (math.floor(360/y))
    return x

n=int(numeroveces())


def cuadrado():
    for i in range(4):
        m.forward(90)
        m.right(90)



def flor_random():
    for i in range (n) :
        m.circle(90)
        m.right(a)



def flor_cuadrada():
    for i in range (n) :
        cuadrado()
        m.right(a)


def poligono():
    l = random.randint(3,14)
    g = int(360/l)

    for i in range (l):
        m.forward(90)
        m.right(g)





def flor_poligono():

    ## valido que g de un poligono susceptible de cerrarse

    while True:
        l = random.randint(3,10)
        g = 360.0/l
        if (g).is_integer() is True:
                             break

    for i in range (n) :


        for i in range (l):
            m.forward(90)
            m.right(g)

        m.right(a)
        m.color(random.random(),random.random(), random.random())



flor_poligono()
#flor_cuadrada()
#flor_random()
m.clear

#flor_cuadrada()
#cuadrado()
