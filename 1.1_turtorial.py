'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(11)  # speed of drawing. Go fast to not waste time.
yoda.setpos(0,-300)
yoda.color("#FFFFFF")
yoda.begin_fill()
yoda.circle(100)  #snowman body
yoda.end_fill()
yoda.penup()
yoda.setpos(0,-100)#middle body
yoda.begin_fill()
yoda.pendown()
yoda.circle(80)
yoda.end_fill()
yoda.penup()
yoda.setpos(0,60)  #head
yoda.begin_fill()
yoda.pendown()
yoda.circle(50)
yoda.end_fill()
yoda.penup()
yoda.goto(0,-50) #snowman buttons
yoda.color('#000000')
yoda.begin_fill()
yoda.pendown()
yoda.circle(10)
yoda.end_fill()
yoda.penup()
yoda.goto(0,-20)
yoda.begin_fill()
yoda.pendown()
yoda.circle(10)
yoda.end_fill()
yoda.penup()
yoda.goto(0,10)
yoda.begin_fill()
yoda.pendown()
yoda.circle(10)
yoda.end_fill()
yoda.penup()
yoda.goto(-15,110) #eyes
yoda.pencolor('#000000')
yoda.pendown()
yoda.circle(15)
yoda.penup()
yoda.goto(-15,115) #pupils
yoda.pendown()
yoda.begin_fill()
yoda.circle(5)
yoda.end_fill()
yoda.penup()
yoda.goto(15,110)
yoda.pendown()
yoda.circle(15)
yoda.penup()
yoda.goto(15,115) #pupils
yoda.pendown()
yoda.begin_fill()
yoda.circle(5)
yoda.end_fill()
yoda.penup()
yoda.goto(-20,85)
yoda.pendown()
yoda.goto(20,85)
yoda.penup()
yoda.goto(0,110)
yoda.pendown() #nose
yoda.color("#FFA500")
yoda.begin_fill()
yoda.goto(40,100)
yoda.goto(0,90)
yoda.goto(0,110)
yoda.end_fill()
yoda.penup()









yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#FFFFFF')


yoda.write('Jaxson Maass',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
