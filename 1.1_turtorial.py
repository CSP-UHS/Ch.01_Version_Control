'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
a change
'''
import turtle
goover=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
goover.goto(100,-50)
goover.speed(10)  # speed of drawing. Go fast to not waste time.
goover.color("#808080")
goover.fillcolor("#808080")
goover.begin_fill()
goover.circle(40)  #wheel one
goover.end_fill()
goover.penup()
goover.setpos(-150,-50) #wheel two
goover.fillcolor("#808080")
goover.begin_fill()
goover.pendown()
goover.circle(40)
goover.end_fill()
goover.penup()
goover.pencolor("#0000FF")
goover.goto(-160,30)
goover.pendown()
goover.fillcolor("#0000FF")
goover.begin_fill()
goover.goto(120,30)
goover.goto(75,175)
goover.penup()
goover.goto(-160,30)
goover.pendown()
goover.goto(-115,175)
goover.goto(75,175)
goover.end_fill()
goover.penup()
goover.pencolor("#ADD8E6")
goover.fillcolor("#A8D9F6")
goover.begin_fill()
goover.goto(80,90)
goover.pendown()
goover.goto(70,130)
goover.goto(-100,130)
goover.goto(-100,90)
goover.goto(80,90)
goover.end_fill()
goover.penup()
goover.goto(170,-160)


goover.write('Aidan',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
