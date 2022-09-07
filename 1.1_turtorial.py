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
yoda.speed(20)  # speed of drawing. Go fast to not waste time.
yoda.color("#37261f")
yoda.penup()


def drawoval(rad):
    for x in range(2):
        yoda.circle(rad, 90)
        yoda.circle(rad // 2, 90)

yoda.setpos(0,-150) #head back
yoda.begin_fill()
yoda.pendown()
yoda.circle(175)
yoda.penup()
yoda.end_fill()
yoda.setpos(-125,100)  #left ear back
yoda.pendown()
yoda.begin_fill()
yoda.circle(60)
yoda.end_fill()
yoda.penup()
yoda.goto(125,100)  #right ear back
yoda.pendown()
yoda.begin_fill()
yoda.circle(60)
yoda.end_fill()
yoda.penup()
yoda.color("#653818")
yoda.setpos(0,-145) #head
yoda.begin_fill()
yoda.pendown()
yoda.circle(170)
yoda.penup()
yoda.end_fill()
yoda.setpos(-125,105)  #left ear
yoda.pendown()
yoda.begin_fill()
yoda.circle(55)
yoda.end_fill()
yoda.penup()
yoda.setpos(125,105)  #right ear
yoda.pendown()
yoda.begin_fill()
yoda.circle(55)
yoda.end_fill()
yoda.penup()
yoda.color("#331800")   #big circle of face
yoda.setpos(0,-115)
yoda.pendown()
yoda.begin_fill()
yoda.circle(140)
yoda.end_fill()
yoda.penup()
yoda.color("#653818") #earse botom of circle of face
yoda.setpos(-140,25)
yoda.begin_fill()
yoda.pendown()
yoda.setpos(140,30)
yoda.setpos(140,-70)
yoda.setpos(100,-70)
yoda.setpos(100,-110)
yoda.setpos(50,-115)
yoda.setpos(-50,-115)
yoda.setpos(-100,-110)
yoda.setpos(-100,-70)
yoda.setpos(-140,-70)
yoda.setpos(-140,30)
yoda.setpos(140,30)
yoda.end_fill()
yoda.penup()
yoda.color("#653818")    #circle earser
yoda.setpos(0,-60)
yoda.begin_fill()
yoda.pendown()
yoda.circle(59)
yoda.color()
yoda.penup()
yoda.end_fill()
yoda.color("#331800")   #left face circle
yoda.setpos(-94.5,0)
yoda.begin_fill()
yoda.pendown()
yoda.circle(44)
yoda.penup()
yoda.end_fill()
yoda.setpos(94.5,0)    #right face circle
yoda.begin_fill()
yoda.pendown()
yoda.circle(44)
yoda.penup()
yoda.end_fill()
yoda.color("#331800")   #nose
yoda.setpos(0,-45)
yoda.pendown()
yoda.begin_fill()
yoda.circle(30)
yoda.end_fill()
yoda.penup()
yoda.setpos(-70,40) #left eye
yoda.pendown()
yoda.begin_fill()
yoda.color("#FFFFFF")
yoda.seth(45)
drawoval(40)
yoda.end_fill()
yoda.penup()
yoda.setpos(100,40) #right eye
yoda.pendown()
yoda.begin_fill()
yoda.color("#FFFFFF")
yoda.seth(45)
drawoval(40)
yoda.end_fill()
yoda.penup()
yoda.setpos(-75,50) #left eye pupil
yoda.pendown()
yoda.begin_fill()
yoda.color("#1D2951")
yoda.seth(45)
drawoval(20)
yoda.end_fill()
yoda.penup()
yoda.setpos(95,50) #right eye pupil
yoda.pendown()
yoda.begin_fill()
yoda.color("#1D2951")
yoda.seth(45)
drawoval(20)
yoda.end_fill()
yoda.penup()
yoda.color("#653818")    #left eye lid
yoda.seth(100)
yoda.setpos(-62,83)
yoda.begin_fill()
yoda.pendown()
yoda.circle(26,210)
yoda.penup()
yoda.end_fill()
yoda.color("#653818")    #right eye lid
yoda.seth(53)
yoda.setpos(109,61)
yoda.begin_fill()
yoda.pendown()
yoda.circle(26,210)
yoda.penup()
yoda.end_fill()

yoda.setpos(0,-175) #sign name
yoda.pendown()
yoda.pencolor('#FF6700')


yoda.write('Matthew Hammerand',font=("Arial", 16, "normal")) # signs your name to your art
yoda.penup()
yoda.setpos(-10,-175)
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
