'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FF00")
yoda.circle(100)  #head
yoda.penup()
yoda.setpos(50,185) #right ear
yoda.pendown()
yoda.goto(200,210)
yoda.goto(88,145)
yoda.penup()
yoda.setpos(-50,185)  #left ear
yoda.pendown()
yoda.goto(-200,210)
yoda.goto(-88,145)
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')


yoda.write('Sign Your Name Here',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
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

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 100, 0, -50)
draw_circle(tommy, "dark green", 50, -75, 0)
draw_circle(tommy, "dark green", 50, 75, 0)
draw_circle(tommy, "black", 25, 75, 0)
draw_circle(tommy, "black", 25, -75, 0)
tommy.goto(0, -50)
tommy.pendown()
tommy.goto(70, 0)
tommy.penup()
draw_circle(tommy, "red", 25, 0, 75)


tommy.penup()
tommy.goto(0,-150)
tommy.color('black')
tommy.write("Sniper Target Tutle", align="center", font=("Arial", 16, "bold"))
tommy.goto(0,-200)
tommy.color('black')
tommy.write("Bam", align="center", font=("Arial", 16, "bold"))
tommy.color('black')

tommy.color('black')
tommy.goto(0,180)
tommy.write('Landen Thompson',font=("Arial", 16, "normal")) # signs your name to your art
tommy.color('black')
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing