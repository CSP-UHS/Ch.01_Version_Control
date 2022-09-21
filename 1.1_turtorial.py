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
screen.bgcolor("white") # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(15)  # speed of drawing. Go fast to not waste time.
yoda.color("blue")
yoda.penup()
yoda.goto(0,0)
yoda.pendown() # start of phone
yoda.forward(200)
yoda.left(90)
yoda.forward(300)
yoda.left(90)
yoda.forward(200)
yoda.left(90)
yoda.forward(300) #end of phone
yoda.penup() #start of swipe up
yoda.goto(85,15)
yoda.pendown()
yoda.color("black")
yoda.left(90)
yoda.forward(60)
yoda.left(90)
yoda.forward(15)
yoda.left(90)
yoda.forward(80)
yoda.left(90)
yoda.forward(15)
yoda.left(90)
yoda.forward(80) #end of phone swipe
yoda.penup()
yoda.goto(30,250) #start of 7
yoda.pendown()
yoda.forward(40)
yoda.right(110)
yoda.forward(40)
yoda.penup() #end of 7
yoda.goto(75,250) # start of :
yoda.pendown()
yoda.circle(5)
yoda.penup() #first :
yoda.goto(75,225)#second :
yoda.pendown()
yoda.circle(5)
yoda.penup() #end of :
yoda.goto(100,240) #start of 0
yoda.pendown()
yoda.circle(20)
yoda.penup() #end of 0
yoda.goto(140,240) # second 0
yoda.pendown()
yoda.circle(20)
yoda.penup() #end of second 0
yoda.goto(15,25) #first circle flashlight
yoda.pendown()
yoda.circle(10)
yoda.penup() #end flashlight
yoda.goto(165,25) #circle camera
yoda.pendown()
yoda.circle(10)
yoda.penup()#end camerca circle
yoda.goto(165,290) # start battery
yoda.pendown()
yoda.left(110)
yoda.forward(15)
yoda.left(90)
yoda.forward(5)
yoda.left(90)
yoda.forward(15)
yoda.left(90)
yoda.forward(5)
yoda.left(90)
yoda.forward(15)
yoda.penup() #end battery
yoda.goto(190,290)
yoda.pendown()
yoda.left(90)
yoda.forward(5)











# yoda.circle(50)  #head
# yoda.penup()
# yoda.setpos(0,60) #right ear
# yoda.pendown()
# yoda.goto(20,75)
# yoda.goto(35,55)
# yoda.penup()
# yoda.setpos(-50,185)  #left ear
# yoda.pendown()
# yoda.goto(-200,210)
# yoda.goto(-88,145)
# yoda.penup()
# yoda.setpos(200,-300)
# yoda.pendown()
# yoda.pencolor('#00FF00')
yoda.penup()
yoda.goto(100,-100)
yoda.write('Benjamin Ordagic',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
