'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

tina = turtle.Turtle()

#head of Alien
tina.penup()
tina.color("light green")
tina.goto(-40,0)
tina.begin_fill()
tina.pendown()
tina.circle(40)
tina.forward(80)
tina.circle(40)
tina.left(90)
tina.forward(80)
tina.left(90)
tina.forward(80)
tina.end_fill()
tina.penup()

#line on head
tina.goto(2,80)
tina.right(90)
tina.pendown()
tina.begin_fill()
tina.forward(50)
tina.left(90)
tina.forward(5)
tina.left(90)
tina.forward(50)
tina.end_fill()

#circle on head
tina.penup()
tina.goto(0,150)
tina.right(90)
tina.pendown()
tina.begin_fill()
tina.circle(10)
tina.end_fill()

#left ear
tina.penup()
tina.goto(-80,30)
tina.pendown()
tina.forward(10)
tina.right(85)
tina.begin_fill()
tina.forward(70)
tina.right(160)
tina.forward(70)
tina.end_fill()

#right ear
tina.penup()
tina.goto(80,30)
tina.left(65)
tina.pendown()
tina.forward(10)
tina.left(85)
tina.begin_fill()
tina.forward(70)
tina.left(160)
tina.forward(70)
tina.end_fill()

#eye whites
tina.penup()
tina.color("white")
tina.goto(13,60)
tina.right(120)
tina.pendown()
tina.begin_fill()
tina.circle(15)
tina.end_fill()

tina.penup()
tina.goto(-25,60)
tina.pendown()
tina.begin_fill()
tina.circle(15)
tina.end_fill()

tina.penup()
tina.goto(51,60)
tina.pendown()
tina.begin_fill()
tina.circle(15)
tina.end_fill()

#eye pupils
tina.penup()
tina.color("black")
tina.goto(-30,50)
tina.pendown()
tina.begin_fill()
tina.circle(7)
tina.end_fill()

tina.penup()
tina.goto(7,50)
tina.pendown()
tina.begin_fill()
tina.circle(7)
tina.end_fill()

tina.penup()
tina.goto(44,50)
tina.pendown()
tina.begin_fill()
tina.circle(7)
tina.end_fill()

#purple neck
tina.penup()
tina.goto(-50,0)
tina.color("purple")
tina.pendown()
tina.begin_fill()
tina.circle(7)
tina.end_fill()
tina.right(125)
tina.penup()
tina.goto(55,-11)
tina.pendown()
tina.begin_fill()
tina.circle(7)
tina.end_fill()
tina.right(180)
tina.begin_fill()
tina.forward(110)
tina.right(90)
tina.forward(13)
tina.right(90)
tina.forward(110)
tina.end_fill()

#body
tina.penup()
tina.color("blue")
tina.goto(0,-141)
tina.pendown()
tina.begin_fill()
tina.circle(65)
tina.end_fill()

tina.penup()
tina.goto(60,-12)
tina.pendown()
tina.begin_fill()
tina.goto(65,-80)
tina.goto(10,-12)
tina.goto(60,-12)
tina.end_fill()

tina.penup()
tina.goto(-60,-12)
tina.pendown()
tina.begin_fill()
tina.goto(-65,-80)
tina.goto(-10,-12)
tina.goto(-60,-12)
tina.end_fill()

#left arm
tina.penup()
tina.goto(-60,-12)
tina.right(120)
tina.pendown()
tina.begin_fill()
tina.forward(60)
tina.left(90)
tina.forward(20)
tina.left(90)
tina.forward(60)
tina.goto(-60,-12)
tina.end_fill()

#right arm
tina.penup()
tina.goto(60,-12)
tina.left(30)
tina.left(210)
tina.pendown()
tina.begin_fill()
tina.forward(60)
tina.right(90)
tina.forward(20)
tina.right(90)
tina.forward(60)
tina.goto(60,-12)
tina.end_fill()

#left palm
tina.penup()
tina.goto(-75,-70)
tina.color("light green")
tina.pendown()
tina.begin_fill()
tina.circle(15)
tina.end_fill()

#right palm
tina.penup()
tina.goto(98,-75)
tina.pendown()
tina.begin_fill()
tina.circle(15)
tina.end_fill()

#bottom lip
tina.penup()
tina.color("black")
tina.goto(-21,20)
tina.pendown()
tina.right(120)
tina.forward(10)
tina.begin_fill()
tina.right(45)
tina.forward(3)
tina.left(45)
tina.forward(4)
tina.right(45)
tina.forward(2)
tina.left(45)
tina.forward(10)
tina.left(45)
tina.forward(2)
tina.right(45)
tina.forward(4)
tina.left(45)
tina.forward(3)
tina.right(45)
tina.forward(10)

#top lip
tina.right(180)
tina.forward(10)
tina.right(45)
tina.forward(3)
tina.left(45)
tina.forward(4)
tina.right(45)
tina.forward(2)
tina.left(45)
tina.forward(10)
tina.left(45)
tina.forward(2)
tina.right(45)
tina.forward(4)
tina.left(45)
tina.forward(3)
tina.right(45)
tina.end_fill()
tina.forward(10)

#words
tina.penup()
tina.goto(-100,-170)
tina.write("Arianna Lear", font=("Arial",16, "normal"))
tina.goto(-120,-170)

turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
