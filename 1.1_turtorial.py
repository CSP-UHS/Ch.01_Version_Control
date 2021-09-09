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
screen.bgcolor("purple") # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#000000")
yoda.begin_fill()
yoda.circle(150)   #head
yoda.end_fill()
yoda.speed(5)
yoda.pendown()
yoda.penup()
yoda.setpos(50,185) #ring finger hole
yoda.pendown()
yoda.color("#800080")
yoda.begin_fill()
yoda.circle(20)
yoda.end_fill()
yoda.penup()
yoda.setpos(-20,185)  #Middle finger hole
yoda.pendown()
yoda.begin_fill()
yoda.circle(20)
yoda.end_fill()
yoda.penup()
yoda.setpos(0,50)
yoda.pendown()
yoda.begin_fill()
yoda.circle(25)    #thumb hole
yoda.end_fill()
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')


yoda.write('Zachary Blum',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
