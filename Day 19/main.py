from turtle_contestans import Contestant
from my_turtle import Screen
import random


screen = Screen()
screen.setup(width=800, height=500)

contestants = [Contestant("cinar"), Contestant("fatma")]
contestants_names = [None] * len(contestants)

count = 0
for c in contestants:
    contestants_names[count] = contestants[count].name
    c.penup()
    c.color(c.random_color())
    count += 1

contestants[0].goto(x=-400, y=100)
contestants[1].goto(x=-400, y=-100)

user_bet = screen.textinput(title="Who will win ?", prompt=f"{contestants_names}")

for c in contestants:
    c.speed("slowest")

winner = ""
finished = False
while not finished:
    for c in contestants:
        c.forward(random.randint(1, 5))

        if c.xcor() >= 390:
            winner = c.name
            finished = True

if winner == user_bet:
    print("You win!")
else:
    print(f"You lose, {winner} wins!")

screen.exitonclick()
