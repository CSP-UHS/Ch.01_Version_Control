'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
matt=turtle.getturtle()
screen=turtle.getscreen()
import math
matt.color('black', "#cccccc")
matt.speed(1000)

clrlist = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen.bgcolor("black")

matt.width(6)
mult = 20
matt.penup()
for i in range(280) :
    matt.forward(2)
    matt.goto((math.sin(i/10)*(200/(i/200+1))),(math.cos(i/10)*(200/(i/200+1))))
    matt.pendown()
    matt.color(str(clrlist[i % 6]))

matt.penup()
matt.goto(-250,-250)
matt.write('Matthew Avis',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
