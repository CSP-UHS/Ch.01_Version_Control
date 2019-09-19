'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
Snow=turtle.Turtle()
screen=turtle.Screen() # makes a screen object turtle
screen.bgcolor('light blue') # colors the screen
Snow.pensize(3) # width of pen line
Snow.speed(10)
Snow.color("white")
Snow.begin_fill()
Snow.circle(50)
Snow.end_fill()
Snow.penup()
Snow.setpos(0,-200)
Snow.pendown()
Snow.begin_fill()
Snow.circle(100)
Snow.end_fill()
Snow.penup()
Snow.color("black")
Snow.goto(0,100)
Snow.pendown()
Snow.begin_fill()
Snow.goto(50,100)
Snow.goto(50,105)
Snow.goto(25,105)
Snow.goto(25,155)
Snow.goto(-25,155)
Snow.goto(-25,105)
Snow.goto(-50,105)
Snow.goto(-50,100)
Snow.goto(0,100)
Snow.end_fill()
Snow.penup()
Snow.setpos(200,-200)
Snow.pendown()
Snow.pencolor('black')
Snow.write('Kenny Flory',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open

