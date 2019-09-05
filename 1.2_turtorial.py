'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("blue")
yoda.circle(101)  #head
yoda.penup()
yoda.setpos(50,185) #right ear
yoda.pendown()
yoda.goto(200,240)
yoda.goto(100,100)
yoda.penup()
yoda.setpos(-50,185)  #left ear
yoda.pendown()
yoda.goto(-200,240)
yoda.goto(-100,100)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('blue')
yoda.write('Henry',font=("Arial", 100, "normal"))



turtle.exitonclick() #Keeps pycharm window open
