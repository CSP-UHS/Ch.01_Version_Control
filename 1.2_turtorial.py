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
yoda.speed(30)  # speed of drawing. Go fast to not waste time.
yoda.setpos(-400,0)
yoda.color("brown")
yoda.begin_fill()
yoda.circle(40)
yoda.end_fill()
yoda.penup()
yoda.setpos(-250,150)
yoda.pendown()
yoda.begin_fill()
yoda.circle(80)
yoda.end_fill()
yoda.penup()
yoda.setpos(0,-200)
yoda.pendown()
yoda.begin_fill()
yoda.circle(120)
yoda.end_fill()
yoda.penup()
yoda.setpos(350,50)
yoda.pendown()
yoda.begin_fill()
yoda.circle(62)
yoda.end_fill()
yoda.penup()
yoda.color("yellow")
yoda.setpos(-400,-60)
yoda.pendown()
yoda.begin_fill()
yoda.circle(5)
yoda.end_fill()
yoda.penup()
yoda.setpos(0,80)
yoda.begin_fill()
yoda.circle(3)
yoda.end_fill()
yoda.penup()
yoda.setpos(-30,110)
yoda.begin_fill()
yoda.circle(8)
yoda.end_fill()
yoda.penup()
yoda.setpos(30,150)
yoda.begin_fill()
yoda.circle(20)
yoda.end_fill()
yoda.penup()
yoda.setpos(300,-90)
yoda.begin_fill()
yoda.circle(30)
yoda.end_fill()
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')
yoda.write('Dylan Smith', font=("Arial", 12, "normal") )


turtle.exitonclick() #Keeps pycharm window open
