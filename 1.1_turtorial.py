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
yoda.pensize(1) # width of pen line
yoda.speed(13)  # speed of drawing. Go fast to not waste time.
yoda.color("white")
yoda.penup()
yoda.goto(0,-150)
yoda.pendown()
yoda.circle(150)
yoda.penup()
yoda.goto(0,-110)
yoda.pendown()
yoda.circle(110)
yoda.penup()
yoda.goto(0,-180)  #main star
yoda.pendown()
yoda.begin_fill()
yoda.goto(30,-30)
yoda.goto(180,0)
yoda.goto(30,30)
yoda.goto(0,180)
yoda.goto(-30,30)
yoda.goto(-180,0)
yoda.goto(-30,-30)
yoda.goto(0,-180)
yoda.end_fill()
yoda.penup()
yoda.goto(0,-25) #details
yoda.color("black")
yoda.pensize(3)
yoda.pendown()
yoda.circle(25)
yoda.pensize(1)
yoda.begin_fill()
yoda.goto(-5,-25)
yoda.goto(0,-150)
yoda.goto(5,-25)
yoda.end_fill()
yoda.penup()
yoda.goto(25,-5)
yoda.pendown()
yoda.begin_fill()
yoda.goto(150,0)
yoda.goto(25,5)
yoda.end_fill()
yoda.penup()
yoda.goto(5,25)
yoda.pendown()
yoda.begin_fill()
yoda.goto(0,150)
yoda.goto(-5,25)
yoda.end_fill()
yoda.penup()
yoda.goto(-25,5)
yoda.pendown()
yoda.begin_fill()
yoda.goto(-150,0)
yoda.goto(-25,-5)
yoda.end_fill()



yoda.write('Matthew Fletcher',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
