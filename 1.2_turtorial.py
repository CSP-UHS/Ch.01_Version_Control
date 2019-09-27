import turtle # without turtle there isn't ocean
DeepSeaSnapper=turtle.Turtle() # the best turtles are underwater
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the background

DeepSeaSnapper.pensize(3) # width of pen line
DeepSeaSnapper.speed(0)  # speed of drawing
DeepSeaSnapper.color("Black") # color of line

#Tic-Tac-Toe Grid
DeepSeaSnapper.penup()
DeepSeaSnapper._rotate(-90)
DeepSeaSnapper.forward(85)
DeepSeaSnapper._rotate(90)
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
DeepSeaSnapper.backward(600)
DeepSeaSnapper.forward(200)
DeepSeaSnapper._rotate(90)
DeepSeaSnapper.forward(200)
DeepSeaSnapper.backward(600)

#Actual Tic-Tac-Toe Game
DeepSeaSnapper.penup()
DeepSeaSnapper._rotate(90)
DeepSeaSnapper.forward(20)
DeepSeaSnapper._rotate(-90)
DeepSeaSnapper.forward(100)
DeepSeaSnapper.pendown()
DeepSeaSnapper.circle(90)

DeepSeaSnapper.penup()
DeepSeaSnapper.forward(200)
DeepSeaSnapper._rotate(-90)
DeepSeaSnapper.forward(210)
DeepSeaSnapper._rotate(90)
DeepSeaSnapper.pendown()
DeepSeaSnapper.circle(90)

DeepSeaSnapper.penup()
DeepSeaSnapper.forward(200)
DeepSeaSnapper._rotate(-90)
DeepSeaSnapper.forward(210)
DeepSeaSnapper._rotate(90)
DeepSeaSnapper.pendown()
DeepSeaSnapper.circle(90)

DeepSeaSnapper.pencolor('Black')
DeepSeaSnapper.write('Danny H',font=("ComicSans", 12, "normal"))
DeepSeaSnapper.penup()
turtle.exitonclick() #Keeps pycharm window open
