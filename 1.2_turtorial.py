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
yoda.color("#00FF00")
yoda.circle(100)  #head
yoda.penup()
yoda.setpos(50,185) #Birds beak
yoda.pendown()
yoda.goto(200,210)
yoda.goto(88,145)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')
yoda.write('Matthew P.',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open
