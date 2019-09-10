'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
kyle=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
kyle.pensize(3) # width of pen line
kyle.speed(10)  # speed of drawing. Go fast to not waste time.
kyle.color("#00FF00")
kyle.circle(100)  #head
kyle.penup()
kyle.setpos(50,180) #right ear
kyle.pendown()
kyle.goto(95,210)
kyle.goto(88,145)
kyle.penup()
kyle.setpos(-50,180)  #left ear
kyle.pendown()
kyle.goto(-95,210)
kyle.goto(-88,145)
kyle.penup()
kyle.goto(50,140)
kyle.pendown()
kyle.shape("circle")
kyle.shapesize(2,4,1)
kyle.fillcolor("white")
kyle.stamp()
kyle.penup()
kyle.goto(-50,140)
kyle.stamp()
kyle.penup()
kyle.setpos(200,-300)
kyle.pendown()
kyle.pencolor('#00FF00')
kyle.write('Lily Burkhead',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open
