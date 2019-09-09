'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
bucky = turtle.Turtle()
bucky.shape("turtle")
bucky.speed(15)
bucky.penup()
bucky.goto(50,-150)
bucky.pendown()
bucky.color("red")
bucky.begin_fill()
bucky.circle(130)
bucky.end_fill()
#first ring
bucky.penup()
bucky.goto(50,-120)
bucky.pendown()
bucky.color("white")
bucky.begin_fill()
bucky.circle(100)
bucky.end_fill()
#second ring
bucky.pendown()
bucky.penup()
bucky.goto(50, -90)
bucky.color("blue")
bucky.begin_fill()
bucky.pendown()
bucky.circle(70)
bucky.end_fill()
#third ring
#tina.pendown()
#tina.penup()
#tina.goto(50, -60)
#tina.pendown()
#tina.circle(40)
#fourth ring
bucky.penup()
bucky.goto(20, -10)
bucky.color("white")
bucky.pendown()
bucky.goto(45, 20)
#first line of star
bucky.begin_fill()
bucky.goto(70, -10)
#second line of star
bucky.goto(100, -10)
#third line of star
bucky.goto(75, -40)
#fourth
bucky.goto(80, -60)
#fifth
bucky.goto(50, -50)
#sixth
bucky.goto(20,-60)
#seventh
bucky.goto(25,-40)
#eighth
bucky.goto(-5,-10)
#ninth
bucky.goto(20,-10)
bucky.end_fill()
bucky.penup()
bucky.goto(80,80)

turtle.exitonclick() #Keeps pycharm window open
