'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

jim = turtle.Turtle()

jim.color('blue')

jim.shape('arrow')

jim.penup()
jim.goto(0,-200)
jim.pendown()
jim.begin_fill()
jim.goto(-200,-200)
jim.goto(-200,200)
jim.goto(200,200)
jim.goto(200,-200)
jim.goto(-200,-200)
jim.end_fill()
jim.penup()

jim.color('white')

jim.goto(-150,200)
jim.pendown()
jim.begin_fill()
jim.goto(-150,175)
jim.goto(-120,175)
jim.goto(-120,-75)
jim.goto(-150,-75)
jim.goto(-150,-100)
jim.goto(125,-100)
jim.goto(125,-40)
jim.goto(95,-40)
jim.goto(95,-75)
jim.goto(-90,-75)
jim.goto(-90,175)
jim.goto(-60,175)
jim.goto(-60,200)
jim.goto(-150,200)
jim.end_fill()
jim.penup()

jim.goto(0,100)
jim.pendown()
jim.begin_fill()
jim.goto(-25,100)
jim.goto(-90,-175)
jim.goto(-120,-175)
jim.goto(-120,-200)
jim.goto(-25,-200)
jim.goto(-25,-175)
jim.goto(-55,-175)
jim.goto(0,70)
jim.goto(0,100)
jim.end_fill()
jim.penup()

jim.goto(0,100)
jim.pendown()
jim.begin_fill()
jim.goto(25,100)
jim.goto(90,-175)
jim.goto(120,-175)
jim.goto(120,-200)
jim.goto(25,-200)
jim.goto(25,-175)
jim.goto(50,-175)
jim.goto(0,70)
jim.end_fill()
jim.penup()

jim.goto(50,150)
jim.write('Carter McInville',font=("Arial", 16, "normal")) # signs your name to your art
jim.goto(200,-200)

turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
done()
