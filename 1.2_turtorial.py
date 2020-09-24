'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
goal=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the screen
goal.pensize(3) # width of pen line
goal.speed(10)  # speed of drawing. Go fast to not waste time.
goal.color("#00FF00")
goal.penup(-200,0) #horizon
goal.setpos()
goal.pendown(-200,0)
goal.goto(200-,0)
goal.goto()
goal.penup()
goal.setpos()
goal.pendown()
goal.goto()
goal.goto()
goal.penup()
goal.setpos()
goal.pendown()
goal.pencolor('#00FF00')


yoda.write('Bryce Getz',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
