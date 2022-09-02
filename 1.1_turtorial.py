'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

tina.goto(-120,-100)
tina.pendown()
tina.goto(120,-100)

#tree1
tina.color("green")
tina.goto(100,-100)
tina.goto(100,-40)
tina.goto(100,-45)
tina.forward(4)
tina.backward(8)
tina.forward(4)
tina.goto(100,-50)
tina.forward(8)
tina.backward(16)
tina.forward(8)
tina.goto(100,-55)
tina.forward(12)
tina.backward(24)
tina.forward(12)
tina.goto(100,-60)
tina.forward(15)
tina.backward(30)
tina.forward(15)
tina.goto(100,-65)
tina.forward(18)
tina.backward(36)
tina.forward(18)
tina.goto(100,-70)
tina.forward(21)
tina.backward(42)
tina.forward(21)
tina.goto(100,-75)
tina.forward(23)
tina.backward(46)
tina.forward(23)
tina.goto(100,-80)
tina.forward(24)
tina.backward(48)
tina.forward(24)
tina.goto(100,-85)
tina.forward(25)
tina.backward(50)
tina.forward(25)
#

tina.color("black")
tina.goto(100,-100)

#tree2
tina.color("green")
tina.goto(50,-100)
tina.goto(50,-40)
tina.goto(50,-45)
tina.forward(4)
tina.backward(8)
tina.forward(4)
tina.goto(50,-50)
tina.forward(8)
tina.backward(16)
tina.forward(8)
tina.goto(50,-55)
tina.forward(12)
tina.backward(24)
tina.forward(12)
tina.goto(50,-60)
tina.forward(15)
tina.backward(30)
tina.forward(15)
tina.goto(50,-65)
tina.forward(18)
tina.backward(36)
tina.forward(18)
tina.goto(50,-70)
tina.forward(21)
tina.backward(42)
tina.forward(21)
tina.goto(50,-75)
tina.forward(23)
tina.backward(46)
tina.forward(23)
tina.goto(50,-80)
tina.forward(24)
tina.backward(48)
tina.forward(24)
tina.goto(50,-85)
tina.forward(25)
tina.backward(50)
tina.forward(25)
#

tina.goto(50,-100)

#Mountain1
tina.goto(20,-100)
tina.color("brown")
tina.begin_fill()
tina.goto(-10,-50)
tina.goto(-40,-100)
tina.end_fill()
tina.color("black")
tina.backward(20)
tina.color("brown")
tina.begin_fill()
tina.goto(-90,-50)
tina.goto(-120,-100)
tina.end_fill()
#

tina.color("black")
tina.penup()

#big mountain
tina.color("grey")
tina.goto(-75,-75)
tina.pendown()
tina.begin_fill()
tina.goto(-50,-40)
tina.goto(-25,-75)
tina.end_fill()
tina.begin_fill()
tina.goto(-75,-75)
tina.goto(-60,-100)
tina.goto(-40,-100)
tina.goto(-25,-75)
tina.goto(-75,-75)
tina.end_fill()
#

tina.color("black")
tina.penup()

#sun
tina.goto(0,-20)
tina.pendown()
tina.color("yellow")
tina.begin_fill()
tina.circle(50)
tina.end_fill()
#

tina.penup()
tina. goto(-150,-150)
tina.color("black")


tina.write('Aidan Zimmerman',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
