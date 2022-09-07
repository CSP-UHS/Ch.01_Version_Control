'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

tina = turtle.Turtle()

tina.hideturtle()

colors = ["red", "red", "red", "red",
"red", "red", "red", "red",
"red", "red", "red", "red",
"red", "red", "red", "red"]

def petals():
  for each_color in colors:
    tina.begin_fill()
    angle = 360 / len(colors)
    tina.color(each_color)
    tina.circle(30)
    tina.end_fill()
    tina.right(angle)
    tina.forward(30)

def stem():
  tina.penup()
  tina.goto(-40,-40)
  tina.begin_fill()
  tina.color('green')
  tina.pendown()
  tina.goto(20,-40)
  tina.goto(20,-200)
  tina.goto(-40,-200)
  tina.goto(-40,-40)
  tina.end_fill()


tina.speed(200)
stem()
tina.penup()
tina.goto(0,150)
tina.pendown()
petals()
tina.penup()
tina.goto(-15,-10)
tina.begin_fill()
tina.pendown()
tina.color('yellow')
tina.circle(85)
tina.end_fill()
tina.penup()
tina.goto(-50,-50)
tina.color('black')


tina.write('Samuel Pattison',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
