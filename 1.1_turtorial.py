'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
import turtle

tina = turtle.Turtle()


tina.color('red')


tina.shape('turtle')


tina.begin_fill()
tina.goto(200,0)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,0)
tina.goto(0,0)
tina.end_fill()

tina.begin_fill()
tina.goto(-200,0)
tina.goto(-200,200)
tina.goto(200,200)
tina.goto(200,0)
tina.end_fill()

tina.goto(0,0)

tina.color("white")

tina.begin_fill()
tina.goto(-200,0)
tina.goto(-200,-20)
tina.goto(200,-20)
tina.goto(200,0)
tina.goto(0,0)
tina.goto(-200,0)
tina.goto(-200,20)
tina.goto(200,20)
tina.goto(200,0)
tina.goto(0,0)
tina.end_fill()

tina.goto(-30,0)
tina.begin_fill()
tina.goto(-35,200)
tina.goto(0,200)
tina.goto(0,-200)
tina.goto(-35,-200)
tina.goto(-35,200)
tina.goto(0,200)
tina.goto(5,200)
tina.goto(5,-200)
tina.goto(0,-200)
tina.goto(0,200)
tina.end_fill()
turtle.exitonclick()


yoda.write('Sign Your Name Here',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
