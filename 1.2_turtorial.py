'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(10) # width of pen line
yoda.speed(15)  # speed of drawing. Go fast to not waste time.
yoda.color('#D5320F')
yoda.begin_fill()
yoda.circle(101)  #head
yoda.end_fill()
yoda.color('#D86113')
yoda.begin_fill()
yoda.circle(80)
yoda.end_fill()
yoda.penup()
yoda.setpos(-50,130)
yoda.pendown()
yoda.circle(20)     #eye
yoda.penup()
yoda.color('black')
yoda.setpos(-53,140)
yoda.begin_fill()
yoda.circle(15)
yoda.end_fill()
yoda.color('#D86113')
yoda.setpos(50,130)
yoda.pendown()
yoda.circle(20)     #eye
yoda.penup()
yoda.color('black')
yoda.setpos(53,140)
yoda.begin_fill()
yoda.circle(15)
yoda.end_fill()
yoda.pensize(3)
yoda.color('#CC724A')
yoda.penup()
yoda.setpos(0,100)
yoda.pendown()
yoda.begin_fill()
yoda.right(120)  # draw mouth
yoda.forward(80)
yoda.left(120)
yoda.forward(80)
yoda.left(120)
yoda.forward(80)
yoda.end_fill()
yoda.penup()
yoda.pensize(5)
yoda.color('red')
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
yoda.setpos(-135,-100)
yoda.pendown()
yoda.pencolor('blue')
yoda.write('Henry',font=("Arial", 100, "normal"))



turtle.exitonclick() #Keeps pycharm window open
