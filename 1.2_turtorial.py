import turtle #Without turtle there isn't ocean
DeepSeaSnapper=turtle.Turtle() #the best turtles are underwater
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the background white

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
yoda.write('Sign Your Name Here',font=("Arial", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open
