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
yoda.pensize(7) # width of pen line
yoda.speed(11)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FFFF")

yoda.penup()

yoda.begin_fill()
yoda.goto(-400,400)
yoda.pd()
yoda.goto(-400,-400)
yoda.goto(400,-400)
yoda.goto(400,400)
yoda.goto(-400,400)
yoda.end_fill()

yoda.pu()

yoda.color("#6E0DD0")
yoda.goto(0,-200)
yoda.pendown()
yoda.begin_fill()
yoda.circle(200)  # First Circle
yoda.end_fill()
yoda.penup()
yoda.goto(0,-250)
yoda.pd()
yoda.begin_fill()
yoda.circle(250)
yoda.end_fill()

yoda.pu()

yoda.color("#00FFFF")
yoda.begin_fill()
yoda.goto(0,25)
yoda.pd()
yoda.goto(-150,-140) #Left Line
yoda.goto(-150,-190)
yoda.goto(0,-25)
yoda.end_fill()

yoda.pu()

yoda.color("#00FFFF")
yoda.begin_fill()
yoda.goto(0,25)
yoda.pd()
yoda.goto(150,-140) #Right Line
yoda.goto(150,-190)
yoda.goto(0,-25)
yoda.end_fill()

yoda.pu()

yoda.goto(-25,200)
yoda.pd()
yoda.color("#00FFFF")
yoda.begin_fill()
yoda.goto(-25,-200) #Strait main line
yoda.goto(25,-200)
yoda.goto(25,200)
yoda.end_fill()

yoda.up()

yoda.color("#0099FF")
yoda.goto(0,-200)
yoda.pendown()
yoda.begin_fill()
yoda.circle(200)  #Circle
yoda.penup()
yoda.goto(0,-250)
yoda.pd()
yoda.circle(250)
yoda.end_fill()

yoda.pu()

yoda.setpos(200,-300)  #Name
yoda.pendown()         #Name
yoda.pencolor('#000000')#Name


yoda.write('Bryce Huey',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
