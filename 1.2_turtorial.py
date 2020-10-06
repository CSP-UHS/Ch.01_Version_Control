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
goal.pensize(5) # width of pen line
goal.speed(5)  # speed of drawing. Go fast to not waste time.
goal.color("black")

 #horizon
goal.pendown()
goal.goto(-200,0)
goal.setpos(200,0)
goal.pendown()
goal.goto(200,0)
#goal
goal.penup()
goal.goto(-75,0)
goal.pendown()
goal.color("grey")
goal.goto(-75,50)
goal.goto(75,50)
goal.goto(75,0)
#ball
goal.penup()
goal.goto(-90,-130)
goal.color("black")
goal.pendown()
goal.circle(50)
goal.penup()
goal.goto(0,-50)




goal.write('Bryce Getz',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
