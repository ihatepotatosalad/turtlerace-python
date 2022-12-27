from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()

user_bet = screen.textinput(
    title='make a bet', prompt='which turtle will win: ')
is_race_on = False
colors = ['red', 'green', 'blue', 'brown', 'orange', 'purple']
all_turtles = []
x = -400
y = -300


for z in range(len(colors)):
    i = Turtle()
    i.penup()
    i.shape('turtle')
    i.color(colors[z])
    i.setposition(x, y)
    all_turtles.append(i)
    y += 50


if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 180:
            winner = turtle.color()
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


if user_bet in winner:
    print('you win')
else:
    print(f'you lose lol {winner} won')

screen.exitonclick()
