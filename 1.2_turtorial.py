'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
drake=turtle.Turtle()

drake.color("lightgreen")
drake.pensize(3)
drake.speed(5)


drake.pendown()
drake.begin_fill()
drake.forward(85)
drake.left(90)
drake.forward(100)
drake.right(90)
drake.forward(10)
drake.left(90)
drake.forward(10)
drake.left(90)
drake.forward(105)
drake.left(90)
drake.forward(10)
drake.left(90)
drake.forward(10)
drake.right(90)
drake.forward(100)
drake.end_fill()
drake.penup()
drake.forward(50)






drake.write('Drake Kimmer',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open
