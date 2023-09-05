'''
1.0 Jedi Training (17pts)  Name:__Walker Lowe__


1. Define Forking (1pt): 
When someone makes a copy of a shared read-only repository.
2. Define Cloning (1pt): 
Making a copy of someone elses repository to work on for yourself
3. Define Branching (1pt):
Multiple strands of a repository that can be worked on simultaneously
4. Define Committing (1pt): 
A checkpoint in the development of a project.
5. Define Merging (1pt): 
Merging is when you fork and clone the code and the owner of the original forked and cloned repository accepts to
merge or in other words use your code
6. Define Pushing (1pt):
Pushing is where we take code from a local branch and bring it to your own remote repository
7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')


tina.penup()
tina.begin_fill()
tina.color('blue')
tina.goto(30,-150)
tina.pendown()
tina.circle(130)
tina.penup()
tina.end_fill()
tina.color('white')
tina.goto(0,0)

tommy.color('white')
tommy.begin_fill()
tommy.pendown()
tommy.circle(30)
tommy.penup()
tommy.end_fill()
tommy.begin_fill()
tommy.color('black')
tommy.pendown()
tommy.circle(20)
tommy.penup()
tommy.end_fill()
tommy.forward(60)
tommy.right(45)
tommy.begin_fill()
tommy.color('white')
tommy.pendown()
tommy.circle(10)
tommy.penup()
tommy.end_fill()
tommy.begin_fill()
tommy.color('black')
tommy.pendown()
tommy.circle(5)
tommy.penup()
tommy.end_fill()
tommy.right(90)
tommy.forward(90)
tommy.begin_fill()
tommy.color('cyan')
tommy.pendown()
tommy.circle(50)
tommy.penup()
tommy.end_fill()
tommy.goto(150,-150)
tommy.write("Yay!")
tommy.forward(20)

tina.color('blue')
tina.goto(-150,-150)
tina.write("We did it!")
tina.backward(20)



tina.goto(150,150)

tina.write('Walker Lowe',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
