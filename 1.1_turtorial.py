'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
penguin=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
penguin.pensize(2) # width of pen line
penguin.speed(5)  # speed of drawing. Go fast to not waste time.
penguin.color("#FFFFFF")
penguin.circle(100)  #head
penguin.penup()
penguin.setpos(75,35) #beak
penguin.pendown()
penguin.goto(200,55)
penguin.goto(96,125)
penguin.penup()
penguin.goto(50,110)  #eye
penguin.pendown()
penguin.circle(25)
penguin.penup()
penguin.goto(50,-236)
penguin.pendown()
def talloval(r):
    penguin.left(45)
    for loop in range(2):
        penguin.circle(r,90)
        penguin.circle(r/2,90)
talloval(150)
penguin.penup()
penguin.goto(200,-150)
penguin.pendown()
talloval(70)
penguin.penup()
penguin.goto(-110,-83)
penguin.pendown()
talloval(70)
penguin.penup()
penguin.goto(-73,-220)
penguin.pendown()
penguin.goto(-73,-275)
penguin.goto(-86,-290)
penguin.goto(-73,-275)
penguin.goto(-73,-290)
penguin.goto(-73,-275)
penguin.goto(-60,-290)
penguin.penup()
penguin.goto(67,-220)
penguin.pendown()
penguin.goto(67,-275)
penguin.goto(54,-290)
penguin.goto(67,-275)
penguin.goto(67,-290)
penguin.goto(67,-275)
penguin.goto(80,-290)
penguin.penup()
penguin.setpos(200,-300)
penguin.pendown()
penguin.pencolor('#900000')


penguin.write('Denis Toric',font=("Times New Roman", 32, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
