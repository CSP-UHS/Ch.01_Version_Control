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
timmy.shapesize(6,3,2)
timmy.pensize(5) # width of pen line
timmy.speed(15) # speed of drawing. Go fast to not waste time.
timmy.hideturtle()
timmy.penup()

timmy.color('#F1134B') #left leg
timmy.setpos(-100,10)
timmy.settiltangle(112.5)
timmy.stamp()

timmy.setpos(100,10) #right leg
timmy.settiltangle(247.5)
timmy.stamp()

timmy.setpos(0,0)
timmy.settiltangle(0)
timmy.pendown()
timmy.color('#E94A88') #Head/body
timmy.begin_fill()
timmy.circle(150)
timmy.end_fill()

timmy.penup() #left arm
timmy.setpos(-120,225)
timmy.settiltangle(22.5)
timmy.stamp()

timmy.setpos(150,150) #right arm
timmy.settiltangle(202.5)
timmy.stamp()

timmy.shapesize(3,2,1) #blush
timmy.color()
timmy.setpos(0,0)
timmy.settiltangle(90)
timmy.stamp()




turtle.exitonclick() #Keeps pycharm window open



'''

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