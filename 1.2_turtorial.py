'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

pencil = turtle
pencil.penup()

pencil.pensize(12)
pencil.goto(0,-150)
pencil.pendown()
pencil.circle(150)
pencil.penup()
pencil.goto(-150,0)
pencil.pendown()
pencil.pensize(10)
pencil.goto(-50,0)
pencil.penup()
pencil.goto(50,0)
pencil.pendown()
pencil.goto(150,0)
pencil.penup()
pencil.pensize(3)
pencil.goto(-25,0)
pencil.penup()
pencil.goto(0,-25)
pencil.pendown()
pencil.circle(25)
pencil.penup()
pencil.goto(0,-49)
pencil.pendown()
pencil.circle(49)
pencil.penup()


turtle.exitonclick() #Keeps pycharm window open
