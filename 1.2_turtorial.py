'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
face=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
face.pensize(3) # width of pen line
face.speed(10)  # speed of drawing. Go fast to not waste time.
face.color("gold")
face.circle(100)  #head
face.penup()
face.setpos(50,185) #right ear
face.pendown()
face.goto(200,210)
face.goto(88,145)
face.penup()
face.setpos(-50,185)  #left ear
face.pendown()
face.goto(-200,210)
face.goto(-88,145)
face.penup()
face.setpos(200,-300)
face.pendown()
face.pencolor('#00FF00')


face.write('Aaron Caltrider',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
