'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
make an edit
'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('blue') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("white")
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
yoda.goto(0,190)
yoda.pendown()
yoda.forward(20)
yoda.backward(40)
yoda.penup()
yoda.goto(0,170)

yoda.pendown()
yoda.pensize(8)
yoda.goto(0,0)
yoda.penup()
yoda.goto(0,120)
yoda.pendown()
yoda.goto(-50,150)
yoda.penup()
yoda.goto(0,120)
yoda.pendown()
yoda.goto(50,150)#arms

yoda.penup()
yoda.goto(0,0)
yoda.pendown()
yoda.pensize(13)
yoda.goto(-70,-150)
yoda.penup()
yoda.goto(0,0)
yoda.pendown()
yoda.goto(70,-150)#legs


yoda.penup()
yoda.goto(200,-150)



yoda.write("matthew",font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
#all done