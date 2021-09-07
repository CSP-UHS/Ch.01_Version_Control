'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FF00")
yoda.penup()
yoda.goto(0,170)
yoda.pendown()
yoda.circle(70)
yoda.penup()
yoda.goto(30,250)
yoda.pendown()
yoda.circle(10)
yoda.penup()
yoda.goto(-30,250)
yoda.pendown()
yoda.circle(10)
yoda.penup()
yoda.goto(0,225)
yoda.pendown()
yoda.goto(-10,215)
yoda.goto(10,210)
yoda.penup()
yoda.goto(0,180)
yoda.pendown()
yoda.circle()



yoda.write('Sign Your Name Here',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
