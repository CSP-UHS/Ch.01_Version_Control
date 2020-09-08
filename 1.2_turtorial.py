'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

draw = turtle.Turtle()
draw.shape ("turtle")

draw.penup()
draw.goto(-100,-90)
draw.pendown()
draw.color("blue")
draw.begin_fill()
draw.forward(300)
draw.left(90)
draw.forward(200)
draw.left(90)
draw.forward(300)
draw.left(90)
draw.forward(200)
draw.end_fill()

draw.penup()
draw.goto(-20,-90)
draw.color("yellow")
draw.left(180)
draw.begin_fill()
draw.pendown()
draw.forward(80)
draw.left(90)
draw.forward(80)
draw.right(90)
draw.forward(40)
draw.right(90)
draw.forward(80)
draw.left(90)
draw.forward(80)
draw.right(90)
draw.forward(40)
draw.right(90)
draw.forward(80)
draw.left(90)
draw.forward(180)
draw.right(90)
draw.forward(40)
draw.right(90)
draw.forward(180)
draw.left(90)
draw.forward(80)
draw.right(90)
draw.forward(40)
draw.end_fill()

draw.penup()
draw.color("black")
draw.goto(-150, -150)
draw.right(180)



draw.write('      Ryan Mullins',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
