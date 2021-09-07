'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
bob = turtle.Turtle()
turtle.bgcolor("Light Blue")
turtle.speed(10)
bob.penup()
bob.goto(-350,35)
bob.color("wheat4")
bob.width(20)
bob.pendown()
bob.begin_fill()
bob.right(90)
bob.forward(360)
bob.left(90)
bob.forward(200)
bob.left(90)
number_list = [1,2,3,4,5,6,7,8,9]
for number in number_list:
    bob.right(5)
    bob.forward(40)
bob.right(45)
bob.forward(80)
bob.left(90)
bob.forward(40)
bob.left(90)
bob.forward(425)
bob.end_fill()
bob.color("Green")
bob.right(180)
bob.width(30)
bob.forward(425)
bob.penup()
bob.left(90)
bob.forward(40)
bob.width(10)
bob.color("Red")
bob.left(90)
bob.forward(40)
bob.right(45)
bob.pendown()
bob.begin_fill()
number_list = [1,2,3,4,5,6,7,8,9]
for number in number_list:
    bob.right(5)
    bob.forward(15)
bob.right(15)
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
for number in number_list:
        bob.right(6)
        bob.forward(5)
number_list = [1,2,3,4,5,6,7,8,9,10]
for number in number_list:
    bob.right(8.5)
    bob.forward(15)
bob.end_fill()
bob.penup()
bob.color("Green")
bob.right(123)
bob.forward(163)
bob.pendown()
bob.width(20)
number_list = [1,2,3,4,5]
for number in number_list:
    bob.left(8.5)
    bob.forward(8)
bob.penup()
bob.color("Black")
bob.goto(240,-320)
screen=turtle.Screen() # makes a screen object
bob.write('Adan Hubby',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
