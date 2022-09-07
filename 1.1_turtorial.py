'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''

import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tommy.color('light blue')
tina.color('yellow')

tommy.penup() #color background
tommy.speed(10)
tommy.goto(-200,200)
tommy.pendown()
tommy.begin_fill()
tommy.goto(200,200)
tommy.goto(200,-200)
tommy.goto(-200,-200)
tommy.goto(-200,200)
tommy.end_fill()

tina.penup() #sun
tina.speed(5)
tina.goto(135,135)
tina.color('yellow')
tina.pendown()
tina.begin_fill()
tina.circle(75)
tina.end_fill()
tina.penup()

tommy.goto(-125,125) #cloud 1
tommy.color('white')
tommy.pendown()
tommy.begin_fill()
tommy.circle(25)
tommy.goto(-95,125)
tommy.circle(25)
tommy.goto(-65,125)
tommy.circle(25)
tommy.end_fill()
tommy.penup()

tommy.goto(-15,90) #cloud 2
tommy.color('white')
tommy.pendown()
tommy.begin_fill()
tommy.circle(25)
tommy.goto(15,90)
tommy.circle(25)
tommy.goto(45,90)
tommy.circle(25)
tommy.end_fill()
tommy.penup()

tina.color('light blue') #tree trunk
tina.goto(-100,-200)
tina.color('brown')
tina.pendown()
tina.begin_fill()
tina.goto(-100,-0)
tina.goto(-50,0)
tina.goto(-50,-200)
tina.goto(-100,-200)
tina.end_fill()
tina.penup()

tina.goto(-125,-75) #tree leaves
tina.color('light green')
tina.penup()
tina.begin_fill()
tina.circle(80)
tina.goto(-25,-75)
tina.circle(80)
tina.goto(-75,-75)
tina.circle(80)
tina.end_fill()

tommy.penup() #sign the picture
tommy.goto(75,-50)
tommy.color('black')
tommy.pendown()
tommy.write("Tommy Hensley")


