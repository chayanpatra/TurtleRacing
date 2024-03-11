from turtle import Turtle, Screen
import random

# Creates Finish Line

line: Turtle = Turtle(visible=False)
screen = Screen()
screen.setup(800, 400)
line.pu()
line.speed('fast')
line.goto(x=230, y=150)
line.pd()
line.right(90)
line.forward(300)
line.pu()
line.goto(x=-300, y=150)
line.pd()

# create instances of turtle
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
y = -70
turtles = []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.pu()
    tim.speed('slow')
    tim.color(colors[i])
    tim.goto(x=-230, y=y)
    y += 30
    turtles.append(tim)
game_on = True
user_bet = screen.textinput(title='Make a bet', prompt="Pick a color: ").lower()
while game_on and user_bet:
    if user_bet.lower() not in colors:
        line.write("Invalid bet.", align="center", font=('Arial', 12, 'normal'))
        break
    else:
        line.write(f"Your bet: {user_bet.title()}", align='center', font=('Arial', 12, 'normal'))
    for turtle in turtles:
        turtle.speed("slowest")
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                won = Turtle(visible=False)
                won.write("You've Won.", align="center", font=('Arial', 12, 'normal'))
            else:
                lost = Turtle(visible=False)
                lost.write(f"You've Lost. Winner is {win_color.title()}.", align="center",
                           font=('Arial', 12, 'normal'))
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
