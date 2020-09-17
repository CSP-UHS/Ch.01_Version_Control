'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
bruh = turtle.Turtle()
bruh.shape('turtle')

bruh.pendown()
bruh.forward(200)
bruh.left(120)
bruh.forward (200)
bruh.left(120)
bruh.forward(200)               # Inner triangle finished
bruh.left(120)
bruh.forward(250)
bruh.left(120)
bruh.forward(350)               # Inner triangle, but extended
bruh.left(180)
bruh.forward(350)
bruh.right(120)
bruh.forward(250)               # Backtrack to inner triangle
bruh.left(60)
bruh.forward(50)
bruh.left(120)
bruh.forward(350)               # Inner triangle, but extended, but again
bruh.left(180)
bruh.forward(350)               # WOAH WE'RE HALFWAY THERE
bruh.right(120)
bruh.forward(250)               # Backtrack to inner triangle, but again
bruh.left(60)
bruh.forward(50)
bruh.left(120)
bruh.forward(350)               # Inner triangle, but extended, but again, but again
bruh.left(120)
bruh.forward(400)               #Backtra- SIKE WE MOVING ON OUT
bruh.left(60)
bruh.forward(50)
bruh.left(60)
bruh.forward(400)
bruh.left(60)
bruh.forward(50)
bruh.left(60)
bruh.forward(400)
bruh.left(60)
bruh.forward(50)                # POG
bruh.penup()
bruh.goto(100, -150)
bruh.write("Penrose Triangle")  # POGROSE TRIANGLE
bruh.goto(100, -175)
bruh.write("Tom Dau")
bruh.goto(100, -200)
turtle.Screen().exitonclick()
#done
