import turtle # without turtle there isn't ocean
DeepSeaSnapper=turtle.Turtle() # the best turtles are underwater
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the background

DeepSeaSnapper.pensize(3) # width of pen line
DeepSeaSnapper.speed(10)  # speed of drawing
DeepSeaSnapper.color("Black") # color of line

DeepSeaSnapper.pendown()

DeepSeaSnapper.penup()

DeepSeaSnapper.pencolor('Black')
DeepSeaSnapper.write('Danny H',font=("ComicSans", 12, "normal"))

turtle.exitonclick() #Keeps pycharm window open
