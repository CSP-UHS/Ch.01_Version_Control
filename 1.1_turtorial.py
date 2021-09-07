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
screen.bgcolor('#87CEEB') # colors the screen
yoda.pensize(100) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.circle(60) #black circle behind head
yoda.fillcolor('#FFFF00')
yoda.color("#FF0000")
yoda.circle(100)  #head
yoda.fillcolor("#00FF00")
yoda.penup()
yoda.goto(-350,-280) #grass
yoda.pencolor('#00FF00')
yoda.pendown()
yoda.goto(350,-280)
yoda.pu()
yoda.setpos(50,185) #right ear
yoda.pencolor('#FF0000')
yoda.pendown()
yoda.goto(200,210)
yoda.goto(88,145)
yoda.penup()
yoda.setpos(50,100) #test for bottom right thing
yoda.pendown()
yoda.goto(220,35)
yoda.goto(35,1)
yoda.penup()
yoda.setpos(-50,185)  #left ear
yoda.pendown()
yoda.goto(-200,210)
yoda.goto(-88,145)
yoda.penup()
yoda.setpos(-50,100) #attempt for bottom left thing
yoda.pendown()
yoda.goto(-220,35) #-200,50
yoda.goto(-35,1) #-100,50
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#FFFFFF')
yoda.penup()

yoda.goto(350,350)
yoda.pensize(100)
yoda.pd()
yoda.pencolor("yellow")
yoda.dot()
yoda.pu()
yoda.pencolor("white")
yoda.goto(-60,100)
#onclick(yoda.write('Kai Baker',font=("Arial", 16, "normal")))
yoda.write('Kai Baker',font=("Arial", 35, "normal")) # signs your name to your art
#turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
yoda.goto(60,-300)
#yoda.pencolor('#FFFF00")
yoda.write('Bottom text',font=("Arial", 16, "normal"))
turtle.exitonclick()

