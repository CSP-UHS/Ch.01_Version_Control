'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

pencil = turtle
pencil.penup()

"""
pencil.speed(30)
x = -10
while x < 10:
    pencil.color("black")
    pencil.goto(x*20,200)
    pencil.pendown()
    pencil.goto(x*20, -200)
    pencil.penup()
    x+=1

y = -10
while y <10:
    pencil.goto(-200,y*20)
    pencil.pendown()
    pencil.goto(200,y*20)
    pencil.penup()
    y+=1
"""


pencil.speed(10)
pencil.color("#252525")
pencil.goto(0,-75)
pencil.pendown()
pencil.shape("circle")
pencil.shapesize(10,15,10)
pencil.stamp()
pencil.shape("turtle")
pencil.shapesize(1,1,1)
pencil.penup()
pencil.hideturtle()
pencil.color("red")
pencil.pensize(12)
pencil.goto(0,-150)
pencil.begin_fill()
pencil.pendown()
pencil.circle(150)
pencil.end_fill()
pencil.penup()
pencil.goto(-150,0)
pencil.pensize(10)
pencil.right(90)
pencil.color("white")
pencil.pendown()
pencil.begin_fill()
pencil.circle(145, 180)
pencil.left(90)
pencil.goto(-150,0)
pencil.end_fill()
pencil.left(180)
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
pencil.color("#ff1a1a")
pencil.goto(0,0)
pencil.pendown()
pencil.begin_fill()
pencil.circle(75)
pencil.end_fill()
pencil.penup()
pencil.goto(20, 75)
pencil.color("#ffe6e6")
pencil.begin_fill()
pencil.circle(15)
pencil.end_fill()
pencil.color("black")
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
pencil.goto(-150,10)
pencil.color("#8a8a8a")
pencil.pensize(12)
pencil.right(90)
pencil.pendown()
pencil.circle(150,180)
pencil.penup()
pencil.left(270)
pencil.goto(0,-150)
pencil.pendown()
pencil.pensize(12)
pencil.color("black")
pencil.circle(150)
pencil.penup()
"""
x=1
while x < 180:
    pencil.forward(2)
    pencil.left(1)
    x+=1

"""
pencil.penup()
pencil.goto(80,-175)
pencil.write("Tristan Holman", 20)
turtle.exitonclick() #Keeps pycharm window open
