import turtle



m=turtle.Turtle()

#m.shape("turtle")
#m.penup()
#m.setpos(-300,-300)
#m.pendown()




#m.peed(1)

#x=600

def triangulo (Turtle,d):
    for i in range(3):
        Turtle.forward(d)
        Turtle.left(120)

def triangulo1 (Turtle,d):
    for i in range(3):
        Turtle.forward(d)
        Turtle.left(120)
    Turtle.left(120)

#triangulo(m,300)


# def tortuga_recursiva():
#     tom = turtle
#     d= 256
#     triangulo(tom,d)


#     for i in range (3):

#         tom.fd(d/2*1)

#         for j in range (1):

#              tom1 = turtle.clone()
#              tom1.left(60)
#              triangulo(tom1,d/2)
#              d= d/2

turtle.speed(6)

def tortuga_sagrada1():
    roberto = turtle
    roberto.color("red")
    d= 256
    triangulo(roberto,d)

     for k in range (3):
        roberto.home()
        d=256
        roberto.left(60*k)
        for i in range (4):


            roberto.fd(d/2*1)


            for j in range (1):
                roberto1 = turtle.clone()
                roberto.left(120)
                #roberto1.left(180)
                triangulo(roberto1,d/2)
                d= d/2




def tortuga_sagrada4():
    roberto = turtle
    roberto.color("red")
    d= 256
    triangulo(roberto,d)

    for i in range (4):


        roberto.fd(d/2*1)


        for j in range (1):
            roberto1 = turtle.clone()
            if j
            roberto.left(120)
            #roberto1.left(180)
            triangulo1(roberto1,d/2)
            d= d/2


def tortuga_sagrada2():
    d=256
    juan = turtle
    juan.penup()
    juan.home()
    juan.pendown()
    juan.fd(d)
    juan.left(120)
    juan.color("blue")
    triangulo(juan,d)


    for i in range (4):


        juan.fd(d/2*1)


        for j in range (1):

             juan1 = turtle.clone()
             juan.left(120)
             #roberto1.left(180)
             triangulo(juan1,d/2)
             d= d/2

def tortuga_sagrada3():
    pepe = turtle
    d= 256
    pepe.penup()
    pepe.home()
    pepe.left(60)
    pepe.pendown()
    pepe.color("green")
    pepe.fd(d)
    pepe.right(180)
    triangulo(pepe,d)


    for i in range (4):


        pepe.fd(d/2*1)


        for j in range (1):

             pepe1 = turtle.clone()
             pepe.left(120)
             #roberto1.left(180)
             triangulo(pepe1,d/2)
             d= d/2





#tortuga_recursiva()
#tortuga_sagrada1()
tortuga_sagrada4()
# tortuga_sagrada2()
# tortuga_sagrada3()
