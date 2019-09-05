'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FF00")
yoda.circle(100)  #head
yoda.penup()
yoda.setpos(50,185) #right ear
yoda.pendown()
yoda.goto(200,210)
yoda.goto(88,145)
yoda.penup()
yoda.setpos(-50,185)  #left ear
yoda.pendown()
yoda.goto(-200,210)
yoda.goto(-88,145)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')
yoda.write('Sign Your Name Here',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open

import turtle
anakin = turtle.Turtle()

screen=turtle.Screen()
screen.bgcolor("green")
anakin.color("silver")
anakin.forward(15)
anakin.right(90)
anakin.forward(10)
anakin.left(90)
anakin.forward(50)
anakin.left(90)
anakin.forward(10)
anakin.right(90)
anakin.forward(100)
anakin.right(90)
anakin.forward(5)
anakin.left(90)
anakin.forward(25)
anakin.left(90)
anakin.forward(5)
anakin.right(90)
anakin.forward(50)

turtle.exitonclick() #Keeps pycharm window open