'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''


import turtle
timmy = turtle.Turtle()
screen = turtle.Screen()  # makes a screen object
screen.bgcolor('black')  # colors the screen
timmy.shape('circle')
timmy.shapesize(6,3,2)
timmy.pensize(5) # width of pen line
timmy.speed(13) # speed of drawing. Go fast to not waste time.
timmy.hideturtle()
timmy.penup()

timmy.color('#F1134B')
timmy.setpos(-100,10) # left leg
timmy.settiltangle(112.5)
timmy.stamp()

timmy.setpos(100,10)  # right leg
timmy.settiltangle(247.5)
timmy.stamp()

timmy.setpos(0,0)
timmy.settiltangle(0)
timmy.pendown()
timmy.color('#FF7EA3')
timmy.begin_fill()
timmy.circle(150)  # head/body
timmy.end_fill()

timmy.penup()
timmy.setpos(-120,225)  # left arm
timmy.settiltangle(22.5)
timmy.stamp()
timmy.setpos(150,150)  # right arm
timmy.settiltangle(202.5)
timmy.stamp()

timmy.shapesize(2,1,2)
timmy.color('#E1265B')
timmy.setpos(75,150)  # right blush
timmy.settiltangle(90)
timmy.stamp()
timmy.setpos(-75,150)  # left blush
timmy.stamp()

timmy.shapesize(3,2,0)
timmy.color('#0E124F')
timmy.settiltangle(0)
timmy.setpos(-30,195)  # left eye 1
timmy.stamp()
timmy.setpos(40,195)  # right eye 1
timmy.stamp()

timmy.shapesize(2.3,2,0)  # right eye 2
timmy.setpos(40,202)
timmy.color('black')
timmy.stamp()
timmy.setpos(-30,202)  # left eye 2
timmy.stamp()

timmy.shapesize(1.9,1.5,0)  # left eye 3
timmy.setpos(-30,206)
timmy.color('white')
timmy.stamp()
timmy.setpos(40,206)  # right eye 3
timmy.stamp()

timmy.color('#F7083F') #Nose
timmy.setpos(30,140)
timmy.pendown()
timmy.begin_fill()
timmy.goto(-20,140)
timmy.goto(5,110)
timmy.goto(30,140)
timmy.end_fill()

timmy.penup()
timmy.setpos(80,-60)
timmy.pendown()
timmy.pencolor('white')
timmy.write('Peggy Y. Barely',font=("Arial", 20, "normal"))



turtle.exitonclick() #Keeps pycharm window open








