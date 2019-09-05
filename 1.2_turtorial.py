'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
timmythicc=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
timmythicc.pensize(3) # width of pen line
timmythicc.speed(10)  # speed of drawing. Go fast to not waste time.
timmythicc.color("#00FF00")
timmythicc.circle(100)  #head
timmythicc.penup()
timmythicc.setpos(50,185) #right ear
timmythicc.pendown()
timmythicc.goto(200,210)
timmythicc.goto(88,145)
timmythicc.penup()
timmythicc.setpos(-50,185)  #left ear
timmythicc.pendown()
timmythicc.goto(-200,210)
timmythicc.goto(-88,145)
timmythicc.penup()
timmythicc.setpos(200,-300)
timmythicc.pendown()
timmythicc.pencolor('#00FF00')
timmythicc.write('Peggy Y. Barely',font=("Arial", 15, "normal"))


turtle.exitonclick() #Keeps pycharm window open
