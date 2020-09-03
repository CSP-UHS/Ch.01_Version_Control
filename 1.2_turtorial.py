'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
freedom = turtle.Turtle()
x = 32.38461538
star = turtle.Turtle()
star.shape('turtle')
freedom.shape('turtle')

star.hideturtle()
freedom.speed(5)
freedom.penup()
freedom.goto(-400,-121)##setting the borders of the flag
freedom.pendown()
freedom.goto(-400,300)
freedom.goto(400,300)
freedom.goto(400,-121)
freedom.goto(-400,-121)

freedom.penup()##creating stripe 1
freedom.goto(400,300)
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("#B22234")
freedom.goto(-105.2631,300)
freedom.goto(-105.2631,(300-x))
freedom.goto(400,(300-x))
freedom.goto(400,300)
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 2
freedom.goto(400,(300-x))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("white")
freedom.goto(-105.2631,(300-x))
freedom.goto(-105.2631,(300-x*2))
freedom.goto(400,(300-x*2))
freedom.goto(400,(300-x))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 3
freedom.goto(400,(300-x*2))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("#B22234")
freedom.goto(-105.2631,(300-x*2))
freedom.goto(-105.2631,(300-x*3))
freedom.goto(400,(300-x*3))
freedom.goto(400,(300-x*2))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 4
freedom.goto(400,(300-x*3))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("white")
freedom.goto(-105.2631,(300-x*3))
freedom.goto(-105.2631,(300-x*4))
freedom.goto(400,(300-x*4))
freedom.goto(400,(300-x*3))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 5
freedom.goto(400,(300-x*4))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("#B22234")
freedom.goto(-105.2631,(300-x*4))
freedom.goto(-105.2631,(300-x*5))
freedom.goto(400,(300-x*5))
freedom.goto(400,(300-x*4))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 6
freedom.goto(400,(300-x*5))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("white")
freedom.goto(-105.2631,(300-x*5))
freedom.goto(-105.2631,(300-x*6))
freedom.goto(400,(300-x*6))
freedom.goto(400,(300-x*7))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 7
freedom.goto(400,(300-x*6))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("#B22234")
freedom.goto(-105.2631,(300-x*6))
freedom.goto(-105.2631,(300-x*7))
freedom.goto(400,(300-x*7))
freedom.goto(400,(300-x*6))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 8
freedom.goto(400,(300-x*7))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("white")
freedom.goto(-400,(300-x*7))
freedom.goto(-400.2631,(300-x*8))
freedom.goto(400,(300-x*8))
freedom.goto(400,(300-x*7))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 9
freedom.goto(400,(300-x*8))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("#B22234")
freedom.goto(-400,(300-x*8))
freedom.goto(-400,(300-x*9))
freedom.goto(400,(300-x*9))
freedom.goto(400,(300-x*8))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 10
freedom.goto(400,(300-x*9))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("white")
freedom.goto(-400,(300-x*9))
freedom.goto(-400.2631,(300-x*10))
freedom.goto(400,(300-x*10))
freedom.goto(400,(300-x*9))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 11
freedom.goto(400,(300-x*10))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("#B22234")
freedom.goto(-400,(300-x*10))
freedom.goto(-400,(300-x*11))
freedom.goto(400,(300-x*11))
freedom.goto(400,(300-x*10))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 12
freedom.goto(400,(300-x*11))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("white")
freedom.goto(-400,(300-x*11))
freedom.goto(-400.2631,(300-x*12))
freedom.goto(400,(300-x*12))
freedom.goto(400,(300-x*11))
freedom.end_fill()
freedom.penup()

freedom.penup()##stripe 13
freedom.goto(400,(300-x*12))
freedom.pendown()
freedom.begin_fill()
freedom.fillcolor("#B22234")
freedom.goto(-400,(300-x*12))
freedom.goto(-400,(300-x*13))
freedom.goto(400,(300-x*13))
freedom.goto(400,(300-x*12))
freedom.end_fill()
freedom.penup()

freedom.begin_fill()##creating the blue box
freedom.fillcolor("#3C3B6E")
freedom.goto(-105.2631,300)
freedom.pendown()
freedom.goto(-105.2631,(300-x*7))
freedom.goto(-400,(300-x*7))
freedom.goto(-400,300)
freedom.goto(-105.2631,300)
freedom.end_fill()
freedom.hideturtle()##hides the turtle when finished

star.showturtle()
star.penup() ##drawing the stars
star.goto(-350, 250)
posx1 = -370
posy1 = 265
posx2 = -345
posy2 = 242.5
incx = 0
incy = 0
stars1 = 0
stars2 = 0
rows1 = 0
rows2 = 0
star.speed(1000)
while rows1 < 5: ##draws the 5 rows of 6
   while stars1 < 6: ##draws the 6 stars
       star.goto(posx1 + incx, posy1 - incy)
       star.pendown()
       star.begin_fill()
       star.fillcolor("white")
       star.pencolor("white")
       star.left(105)
       star.fd(25)
       star.left(145)
       star.fd(25)
       star.left(145)
       star.fd(25)
       star.left(145)
       star.fd(25)
       star.left(145)
       star.end_fill()
       star.penup()
       star.end_fill()
       star.home()
       stars1 = stars1 + 1
       incx = incx + 50
   incx = 0
   incy = incy + 45
   rows1 = rows1 + 1
   stars1 = 0
incx = 0
incy = 0
while rows2 < 4: ##draws the 4 rows
   while stars2 < 5: ##draws the 5 stars
       star.goto(posx2 + incx, posy2 - incy)
       star.pendown()
       star.begin_fill()
       star.fillcolor("white")
       star.pencolor("white")
       star.left(105)
       star.fd(25)
       star.left(145)
       star.fd(25)
       star.left(145)
       star.fd(25)
       star.left(145)
       star.fd(25)
       star.left(145)
       star.end_fill()
       star.penup()
       star.end_fill()
       star.home()
       stars2 = stars2 + 1
       incx = incx + 50
   incx = 0
   incy = incy + 45
   rows2 = rows2 + 1
   stars2 = 0

star.speed(5)##writing name
star.pensize(10)
star.penup()
star.color("black")
star.goto(-375,325)
star.write("USA! USA! USA! USA! USA! USA!", font=("Comic Sans",36,"bold"))
star.goto(0,-150)
star.write("      Alex Mears")

turtle.Screen().exitonclick()##keeping the window open until it finishes and I click to exit


