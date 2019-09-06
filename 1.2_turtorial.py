'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
fish=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
fish.pensize(3) # width of pen line
fish.speed(2)  # speed of drawing. Go fast to not waste time.
fish.color("#0000A0")
fish.circle(85)
fish.circle(85,-85)
fish._rotate(-45)
fish.forward(150)
fish._rotate(135)


fish.write('Rowdy Alexander',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open
