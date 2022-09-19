
import turtle


tina = turtle.Turtle()


tina.color('red')


tina.shape('turtle')


tina.begin_fill()
tina.goto(300,0)
tina.goto(300,-200)
tina.goto(-200,-200)
tina.goto(-200,0)
tina.goto(0,0)
tina.end_fill()

tina.begin_fill()
tina.goto(-200,0)
tina.goto(-200,200)
tina.goto(300,200)
tina.goto(300,0)
tina.end_fill()

tina.goto(0,0)

tina.color("white")

tina.begin_fill()
tina.goto(-200,0)
tina.goto(-200,-20)
tina.goto(300,-20)
tina.goto(300,0)
tina.goto(0,0)
tina.goto(-200,0)
tina.goto(-200,20)
tina.goto(300,20)
tina.goto(300,0)
tina.goto(0,0)
tina.end_fill()

tina.goto(-30,0)
tina.begin_fill()
tina.goto(-35,200)
tina.goto(0,200)
tina.goto(0,-200)
tina.goto(-35,-200)
tina.goto(-35,200)

tina.end_fill()
tina.color("black")
tina.write('Andrew Donoho',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing


