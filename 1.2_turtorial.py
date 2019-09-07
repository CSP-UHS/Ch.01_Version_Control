'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
cal=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
cal.speed(10)
cal.penup()
cal.setpos(100,50)
cal.color('white')
cal.pendown()
cal.begin_fill()
cal.left(90)
cal.circle(100,180)
cal.left(90)
cal.forward(200)
cal.end_fill()
cal.color('gray')
cal.begin_fill()
cal.right(135)
cal.forward(30)
cal.right(45)
cal.penup()
cal.setpos(-100,50)
cal.left(135)
cal.pendown()
cal.forward(30)
cal.left(45)
cal.forward(160)
cal.penup()
cal.setpos(-100,50)
cal.pendown()
cal.forward(200)
cal.end_fill()
cal.color('black')
cal.backward(200)
cal.penup()
cal.setpos(5,90)
cal.left(20)
cal.begin_fill()
cal.pendown()
cal.circle(20)
cal.end_fill()
cal.penup()
cal.color('yellow')
cal.penup()
cal.write('Cal Watson',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open
