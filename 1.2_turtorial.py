'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
bucky = turtle.Turtle()
bucky.shape("turtle")
bucky.speed(10)
bucky.penup()
bucky.goto(50,-150)
bucky.pendown()
bucky.circle(130)
#first ring
bucky.penup()
bucky.goto(50,-120)
bucky.pendown()
bucky.circle(100)
#second ring
bucky.pendown()
bucky.penup()
bucky.goto(50, -90)
bucky.pendown()
bucky.circle(70)
#third ring
#tina.pendown()
#tina.penup()
#tina.goto(50, -60)
#tina.pendown()
#tina.circle(40)
#fourth ring
bucky.penup()
bucky.goto(38, -10)
bucky.pendown()
bucky.goto(41, -5)


turtle.exitonclick() #Keeps pycharm window open
