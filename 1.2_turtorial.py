'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
impossible_triangle=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the screen
impossible_triangle.pensize(3) # width of pen line
impossible_triangle.speed(10)  # speed of drawing. Go fast to not waste time.
impossible_triangle.color('black')
impossible_triangle.penup()
impossible_triangle.goto(-200,-200)
impossible_triangle.pendown()
impossible_triangle.goto(200,-200)
impossible_triangle.goto(253,-130)
impossible_triangle.goto(40,200)
impossible_triangle.goto(-40,200)
impossible_triangle.goto(-253,-130)
impossible_triangle2=turtle.Turtle()
impossible_triangle2.pensize(3)
impossible_triangle2.speed(10)
impossible_triangle2.penup()
impossible_triangle2.goto(-40,200)
impossible_triangle2.pendown()
impossible_triangle2.goto(150,-80)
impossible_triangle2.goto(-70,-80)
impossible_triangle2.goto(-18,5)
impossible_triangle2.goto(25,-80)
impossible_triangle2.goto(-18,5)
impossible_triangle2.goto(-70,-80)
impossible_triangle2.goto(-100,-130)
impossible_triangle2.goto(253,-130)
impossible_triangle3=turtle.Turtle()
impossible_triangle3.pensize(3)
impossible_triangle3.speed(10)
impossible_triangle3.penup()
impossible_triangle3.goto(25,-80)
impossible_triangle3.pendown()
impossible_triangle3.goto(-18,5)
impossible_triangle3.goto(-42,50)
impossible_triangle.goto(-200,-200)
impossible_triangle.pendown()
impossible_triangle.pencolor('black')


impossible_triangle.write('Sign Your Name Here',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
