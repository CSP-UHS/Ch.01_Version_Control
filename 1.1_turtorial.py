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

yoda.penup()
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#FFFFFF")
yoda.goto(0,100)
yoda.pendown()  #head
yoda.circle(50)
yoda.goto(0,-100)
yoda.penup()
yoda.goto(0,50)
yoda.pendown()
yoda.goto(100,0)
yoda.goto(0,50)
yoda.goto(-100,0)
yoda.penup()
yoda.goto(0,-100)
yoda.pendown()
yoda.goto(50,-200)
yoda.goto(0,-100)
yoda.goto(-50,-200)
yoda.penup()
yoda.goto(0,150)
yoda.pendown()
yoda.goto(-5,135)
yoda.goto(0,135)
yoda.penup()
yoda.goto(-20,155)
yoda.pendown()
yoda.circle(10)
yoda.penup()
yoda.goto(20,155)
yoda.pendown()
yoda.circle(10)
yoda.penup()
yoda.goto(-30,165)
yoda.pendown()
yoda.goto(-50,165)
yoda.penup()
yoda.goto(-10,165)
yoda.pendown()
yoda.goto(10,165)
yoda.penup()
yoda.goto(30,165)
yoda.pendown()
yoda.goto(50,165)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#FF00FF')


yoda.write('Gavin Clarkson',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
yoda.penup()