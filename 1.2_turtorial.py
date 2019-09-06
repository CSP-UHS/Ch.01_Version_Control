'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.right(90)
tina.forward(180)
tina.right(90)
tina.forward(180)
tina.right(90)

tina.pendown()
tina.pencolor("red")
tina.forward(300)
tina.right(90)
tina.pencolor("orange")
tina.forward(300)
tina.right(90)
tina.pencolor("yellow")
tina.forward(250)
tina.right(90)
tina.pencolor("green")
tina.forward(250)
tina.right(90)
tina.pencolor("blue")
tina.forward(251)
tina.right(135)
tina.pencolor("indigo")
tina.forward(130)
tina.right(45)
tina.pencolor("violet")
tina.forward(110)
tina.right(62)
tina.pencolor("red")
tina.forward(105)

tina.penup()
tina.backward(90)
tina.right(180)
tina.forward(17)
tina.right(28)

tina.pendown()
tina.pencolor("orange")
tina.forward(90)
tina.right(38)
tina.pencolor("yellow")
tina.forward(85)
tina.backward(85)
tina.left(128)
tina.pencolor("green")
tina.forward(110)
tina.right(37)
tina.pencolor("blue")
tina.forward(112)
tina.backward(112)
tina.left(127)
tina.pencolor("indigo")
tina.forward(90)


turtle.exitonclick() #Keeps pycharm window open
