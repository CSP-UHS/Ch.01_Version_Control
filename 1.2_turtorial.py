'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''

import turtle
jake = turtle.Turtle()
screen = turtle.Screen() # makes a screen object
screen.bgcolor('sky blue') # colors the screen


jake.pensize(10) # width of pen line
jake.speed(10)  # speed of drawing. Go fast to not waste time.
jake.color("#9AFFF3", "#7affb4")
jake.begin_fill()
jake.circle(200)
jake.end_fill()
jake.penup()

jake.color("#9AFFF3", "#9AFFF3")
jake.setpos(0, 25)
jake.pendown()
jake.begin_fill()
jake.circle(15)
jake.end_fill()
jake.penup()
jake.setpos(15, 100)
jake.pendown()
jake.begin_fill()
jake.circle(25)
jake.end_fill()
jake.penup()
jake.setpos(-15, 100)
jake.pendown()
jake.begin_fill()
jake.circle(12)
jake.end_fill()
jake.penup()

jake.setpos(75, 205)
jake.pendown()
jake.circle(10)
jake.circle(100, 100)
jake.penup()
jake.setpos(15,100)
jake.pendown()
jake.circle(10)
jake.penup()
jake.setpos(-75, 205)
jake.pendown()
jake.circle(10)


jake.penup()
jake.setpos(50, 250) #right ear
jake.pendown()
jake.goto(200, 210)
jake.goto(88, 145)
jake.penup()
jake.setpos(-50, 250)  #left ear
jake.pendown()
jake.goto(-200, 210)
jake.goto(-88, 145)
jake.penup()
jake.setpos(200, -300)
jake.pendown()



jake.write('Jake',font=("Arial", 56, "bold")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
