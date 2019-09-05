'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

pencil = turtle
pencil.penup()
pencil.speed(5)

pencil.color("red")
pencil.pensize(12)
pencil.goto(0,-150)
pencil.begin_fill()
pencil.pendown()
pencil.circle(150)
pencil.end_fill()
pencil.penup()
pencil.goto(-150,0)
pencil.right(90)
pencil.color("white")
pencil.pendown()
pencil.begin_fill()
pencil.circle(150, 180)
pencil.left(90)
pencil.goto(-150,0)
pencil.end_fill()
pencil.color("black")
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
pencil.goto(0,-50)
pencil.pendown()
pencil.begin_fill()
pencil.circle(50)
pencil.end_fill()
pencil.penup()
pencil.goto(0,-25)
pencil.color("white")
pencil.pendown()
pencil.begin_fill()
pencil.circle(25)
pencil.end_fill()
pencil.penup()
pencil.goto(0,-150)
pencil.pendown()
pencil.pensize(12)
pencil.color("black")
pencil.circle(150)


turtle.exitonclick() #Keeps pycharm window open
