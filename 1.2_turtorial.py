'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

yoda = turtle.Turtle()

yoda.speed(20)
yoda.color('peach puff')
yoda.penup()
yoda.goto(200,200)
yoda.pendown()
yoda.begin_fill()
yoda.goto(200,-200)
yoda.goto(-200,-200)
yoda.goto(-200,200)
yoda.end_fill()

yoda.color('orange')

yoda.shape('turtle')
yoda.penup()
yoda.goto(-200,200)
yoda.pendown()
yoda.begin_fill()
yoda.goto(200,200)
yoda.goto(200,0)
yoda.goto(150,0)
yoda.goto(150,50)
yoda.goto(100,50)
yoda.goto(100,100)
yoda.goto(0,100)
yoda.goto(0,50)
yoda.goto(-50,50)
yoda.goto(-50,0)
yoda.goto(-200,0)
yoda.end_fill()

yoda.penup()
yoda.color('white')
yoda.goto(-150,-50)
yoda.begin_fill()
yoda.goto(-150,0)
yoda.goto(-100,0)
yoda.goto(-100,-50)
yoda.end_fill()

yoda.penup()
yoda.goto(150,0)
yoda.begin_fill()
yoda.goto(150,-50)
yoda.goto(100,-50)
yoda.goto(100,0)
yoda.end_fill()

yoda.penup()
yoda.color('green')
yoda.goto(100,0)
yoda.begin_fill()
yoda.goto(100,-50)
yoda.goto(50,-50)
yoda.goto(50,0)
yoda.end_fill()

yoda.penup()
yoda.goto(-50,0)
yoda.begin_fill()
yoda.goto(-50,-50)
yoda.goto(-100,-50)
yoda.goto(-100,0)
yoda.end_fill()

yoda.penup()
yoda.color('light pink')
yoda.goto(-50,-100)
yoda.begin_fill()
yoda.goto(50,-100)
yoda.goto(50,-150)
yoda.goto(-50,-150)
yoda.end_fill()


yoda.write('James Hmar',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
