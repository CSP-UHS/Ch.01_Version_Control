'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
timmy=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
timmy.shape('circle')
timmy.shapesize(5,2,1)
timmy.pensize(3) # width of pen line
timmy.speed(10) # speed of drawing. Go fast to not waste time.
timmy.color('#E94A88')
timmy.begin_fill()
timmy.circle(150)
timmy.end_fill()
timmy.penup()



turtle.exitonclick() #Keeps pycharm window open


'''

timmythicc.setpos(50,185)
timmythicc.pendown()
timmythicc.goto(200,210)
timmythicc.goto(88,145)
timmythicc.penup()
timmythicc.setpos(-50,185)
timmythicc.pendown()
timmythicc.goto(-200,210)
timmythicc.goto(-88,145)
timmythicc.penup()
timmythicc.setpos(200,-300)
timmythicc.pendown()
timmythicc.pencolor('blue')
timmythicc.write('Peggy Y. Barely',font=("Arial", 15, "normal"))




'''