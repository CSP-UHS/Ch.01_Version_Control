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

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')

tina.begin_fill()
tina.goto(200,0)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,0)
tina.goto(0,0)
tina.end_fill()

tommy.penup()
tommy.goto(-70,100)
tommy.write("Tina, let's Make a picture together!")
tommy.goto(120,130)


tina.penup()
tina.color('white')
tina.goto(-40,-100)
tina.write("Alright, I'm ready!!")
tina.goto(0,-130)
tina.pendown()

tommy.penup()
tommy.begin_fill()
tommy.goto(120,130)
tommy.color("yellow")
tommy.pendown()
tommy.circle(30)
tommy.penup()
tommy.end_fill()
tommy.goto(70,170)
tommy.pendown()
tommy.goto(30,170)
tommy.penup()
tommy.goto(120,110)
tommy.pendown()
tommy.goto(120,70)
tommy.penup()
tommy.goto(170,170)
tommy.pendown()
tommy.goto(200,170)


tommy.write('Ava Binstock',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
