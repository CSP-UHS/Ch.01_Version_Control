'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

def draw_rectangle(turtle, color, x1, y1, x2, y2):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x1,y1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(x1,y2)
    turtle.goto(x2,y2)
    turtle.goto(x2,y1)
    turtle.goto(x1,y1)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

tom = turtle.Turtle()
tom.shape("turtle")
tom.speed(500)

draw_circle(tom, "yellow", 200, 0, -12)  #makes outer circle
draw_circle(tom, "white", 185, 0, 0)
draw_rectangle(tom, "yellow", -200, 180, -30, 190)  #makes horizontal line
draw_rectangle(tom, "yellow", -5, 20, 5, 380)    #makes vertical line
draw_rectangle(tom, "white", -5, 360, -15, 400)   #makes the little space at the top

tom.penup() #making the bottom of the "Q"
tom.color("yellow")
tom.fillcolor("yellow")
tom.goto(10, 0)
tom.begin_fill()
tom.pendown()
tom.goto(150, -51)
tom.goto(225, -61)
tom.goto(201, -68)
tom.goto(152,-70)
tom.goto(100, -60)
tom.goto(30, -30)
tom.goto(0,-25)
tom.goto(-50, -30)
tom.goto(-58, -28)
tom.goto(-55,-20)
tom.goto(-20,0)
tom.goto(10,0)
tom.penup()
tom.end_fill()

tom.penup()
tom.goto(0,-120)
tom.color('black')
tom.write("Ryan Muetzel", align="center", font=(None, 16, "bold"))
tom.goto(420,-400)
tom.write("RIP TOM 2.0", align="center", font=(None, 12))  #hehe
tom.goto(0,-160)

turtle.Screen().exitonclick()