'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
tim = turtle.Turtle()
tim.shape("square")

def LIE():  # the cake is a lie
    tim.penup()
    tim.speed(20)
    column = [-275,-138,2,140]
    tim.color("#bb0a1e")
    tim.seth(270)
    for number in column:
        tim.goto(number, 190)
        for loop in range(20):
            tim.write("THE CAKE IS A LIE",font=("times new roman",16,"italic"))
            tim.forward(20)

def oval(r):  # draws oval
    tim.pendown()
    for loop in range(2):
        tim.circle(r / 4, 45)
        tim.circle(r / 2, 15)
        tim.circle(r, 60)
        tim.circle(r / 2, 15)
        tim.circle(r / 4, 45)

def half_oval(r):  # draws half oval
    tim.pendown()
    tim.circle(r / 4, 45)
    tim.circle(r / 2, 15)
    tim.circle(r, 60)
    tim.circle(r / 2, 15)
    tim.circle(r / 4, 45)

def candy_cherry():
    tim.pendown()  # cherry
    tim.color("red")
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()
    tim.penup()

def cream():
    tim.color("white")  # whipped cream
    tim.begin_fill()
    oval(30)
    tim.end_fill()
    tim.color("black")
    oval(30)

def bake():
    tim.penup()  # draws main part of cake
    tim.color("#693a24")  # chocolate color
    tim.goto(-135, -75)  # starting point
    tim.right(90)
    tim.begin_fill()
    half_oval(200)  # bottom of cake
    tim.forward(75)  # right side
    half_oval(200)  # top
    tim.forward(75)  # left side
    tim.end_fill()
    tim.color("black")  # outline
    half_oval(200)  # bottom
    tim.forward(75)  # right side
    oval(200)  # top rim
    tim.penup()
    half_oval(200)  # moves to right side
    tim.pendown()
    tim.forward(75)  # right side
    tim.penup()

def cherry():
    tim.seth(180)  # centers cream
    tim.forward(20)
    tim.seth(270)  # properly orients cream
    cream()
    tim.penup()
    tim.seth(0)  # centers cherry
    tim.forward(30)  # centers cherry
    tim.left(90)  # centers cherry
    tim.forward(5)  # centers cherry
    candy_cherry()  # and a cherry on top

def candle():
    tim.penup()  # whipped cream at candle base
    tim.goto(-13, 5)
    tim.seth(270)
    tim.color("white")
    tim.begin_fill()
    oval(20)
    tim.end_fill()
    tim.color("black")
    oval(20)
    tim.penup()
    tim.goto(-6, 5)  # candlestick
    tim.seth(270)
    tim.color("white")
    tim.begin_fill()
    half_oval(10)
    tim.forward(75)
    oval(10)
    half_oval(10)
    tim.forward(75)
    tim.end_fill()
    tim.color("black")
    half_oval(10)
    tim.forward(75)
    oval(10)
    half_oval(10)
    tim.forward(75)
    tim.penup()  # flame
    tim.goto(0, 80)
    tim.seth(0)
    tim.pendown()
    tim.begin_fill()
    tim.color("orange")
    tim.circle(6, 90)
    tim.goto(0, 110)
    tim.goto(-6, 86)
    tim.seth(270)
    tim.circle(6, 90)
    tim.end_fill()
    tim.goto(0, 82)
    tim.color("yellow")  # inner flame
    tim.begin_fill()
    oval(5)
    tim.end_fill()
    tim.penup()

def sign():
    tim.color("white")  # box
    tim.goto(270, -210)
    tim.seth(90)
    tim.pendown()
    tim.begin_fill()
    tim.forward(20)
    tim.left(90)
    tim.forward(85)
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(85)
    tim.end_fill()
    tim.color("black")  # outline
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(85)
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(85)
    tim.penup()
    tim.back(80)
    tim.right(90)
    tim.back(1)
    tim.write("Joe Schmidt",font=("times new roman",16,"normal"))
    tim.back(9)         # moves tim next to name
    tim.right(90)
    tim.forward(15)

tim.speed(20)
bake()
tim.penup()
tim.goto(42, 60)  # places cherries
cherry()
tim.goto(100, 32)
cherry()
tim.goto(100, -22)
cherry()
tim.goto(42, -50)
cherry()
tim.goto(-42, -50)
cherry()
tim.goto(-100, -22)
cherry()
tim.goto(-100, 32)
cherry()
tim.goto(-42, 60)
cherry()
candle()
LIE()
sign()

turtle.exitonclick() #Keeps pycharm window open so we can see the drawing