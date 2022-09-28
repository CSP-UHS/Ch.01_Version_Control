'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

tina=turtle.Turtle()
tina.shape('turtle')

tommy=turtle.Turtle()
tommy.shape('turtle')

tommy.penup()
tommy.goto(0,-120)
tommy.begin_fill()
tommy.color("red")
tommy.pendown()
tommy.circle(120)
tommy.end_fill()
tommy.penup()
tommy.goto(80,-150)

tina.color('gold')
tina.begin_fill()
tina.right(45)
tina.forward(80)
tina.right(135)
tina.forward(110)
tina.right(135)
tina.goto(0,0)
tina.end_fill()
tina.forward(80)
tina.left(135)
tina.forward(110)
tina.left(135)
tina.goto(0,0)
tina.penup()
tina.goto(-80,-150)
tina.left(45)

tina.write('Tanner Evitts',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
