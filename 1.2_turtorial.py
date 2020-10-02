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
screen.bgcolor('navy') # colors the screen
yoda.pensize(5) # width of pen line
yoda.speed(5)  # speed of drawing. Go fast to not waste time.
yoda.color("#000000")
yoda.penup()
yoda.setpos(-20,150)#first shape
yoda.pendown()
yoda.goto(-20,150)
yoda.goto(10,120)
yoda.penup()
yoda.setpos(10,120)
yoda.pendown()
yoda.goto(10,120)
yoda.goto(-120,-20)
yoda.penup()
yoda.setpos(-120,-20)
yoda.pendown()
yoda.goto(-120,-20)
yoda.goto(-120,50)
yoda.penup()
yoda.setpos(-120,50)
yoda.pendown()
yoda.goto(-120,50)
yoda.goto(-20,150)
yoda.penup()

yoda.setpos(-65,-10)#second shape
yoda.pendown()
yoda.goto(-65,-10)
yoda.goto(-165,-110)
yoda.penup()
yoda.setpos(-165,-110)
yoda.pendown()
yoda.goto(-165,-110)
yoda.goto(-165,-180)
yoda.penup()
yoda.setpos(-165,-180)
yoda.pendown()
yoda.goto(-165,-180)
yoda.goto(-35,-40)
yoda.penup()
yoda.setpos(-35,-40)
yoda.pendown()
yoda.goto(-35,-40)
yoda.goto(-65,-10)
yoda.penup()
yoda.pencolor('#000000')
yoda.setpos(200,-200)



yoda.write('Gerardo Lopez',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
