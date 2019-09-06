import turtle #Without turtle there isn't ocean
DeepSeaSnapper=turtle.Turtle() #the best turtles are underwater
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the background white

DeepSeaSnapper.pensize(3) # width of pen line
DeepSeaSnapper.speed(10)  # speed of drawing
DeepSeaSnapper.color("Black")

DeepSeaSnapper.pendown()

DeepSeaSnapper.penup()



DeepSeaSnapper.pencolor('#Purple')
DeepSeaSnapper.write('Sign Your Name Here',font=("ComicSans", 12, "normal"))


turtle.exitonclick() #Keeps pycharm window open
