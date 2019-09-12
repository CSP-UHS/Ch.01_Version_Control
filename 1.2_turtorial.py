import turtle # without turtle there isn't ocean
DeepSeaSnapper=turtle.Turtle() # the best turtles are underwater
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the background

DeepSeaSnapper.pensize(3) # width of pen line
DeepSeaSnapper.speed(0)  # speed of drawing
DeepSeaSnapper.color("Black") # color of line

#Trying to make tic tac toe gif
DeepSeaSnapper.pendown()
DeepSeaSnapper.backward(300)
DeepSeaSnapper.forward(600)
DeepSeaSnapper.backward(200)
DeepSeaSnapper._rotate(-90)
DeepSeaSnapper.forward(200)
DeepSeaSnapper.backward(600)
DeepSeaSnapper.forward(200)
DeepSeaSnapper._rotate(90)
DeepSeaSnapper.forward(200)

DeepSeaSnapper.pencolor('Black')
DeepSeaSnapper.write('Danny H',font=("ComicSans", 12, "normal"))
DeepSeaSnapper.penup()
turtle.exitonclick() #Keeps pycharm window open
