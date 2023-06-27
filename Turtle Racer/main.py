from turtle import *
import random
from playsound import playsound
import tkinter as tk
import race_track

rt = race_track
bgcolor("green")
screen = Screen()
screen.setup(width=800, height=500)
colors = ["red", "blue", "green", "yellow", "purple", "orange", "coral", "aqua", "darkblue", "pink"]
user_bet = screen.textinput(title=f"🚨🐢🚨PLACE YOUR BETS🚨🐢🚨\n", prompt=f"Which turtle will win the race? Enter a color: \n{' '.join(colors)}\n")
y_pos = [-130, -100, -70, -40, -10, 20, 50, 80, 110, 140]
my_turtles = []

def play_sound():
    playsound("/Users/erictyler/Turtle Racer/Theme Music.mp3", False)

play_sound()


def celebrate():
    turtle.speed(100)
    turtle.setheading(270)
    turtle.forward(10)
    for i in range(50):
        turtle.left(10)
        turtle.forward(1)

race_track.draw_track()

for turtle_index in range (0, 10):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    my_turtles.append(new_turtle)


if user_bet:
    race_on = True

playsound("/Users/erictyler/Turtle Racer/321go.mp3")

while race_on:
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            turtle.goto(0,0)
            turtle.write(f"{winner} wins the race!", align="center", font=("Arial", 20, "normal"))
            celebrate()
            race_on = False
            if winner == user_bet:
                playsound("/Users/erictyler/Turtle Racer/victory.mp3", False)
                tk.messagebox.askyesno(title="WINNER", message=f"💰💰💰YOU WIN {winner} WON THE RACE💰💰💰\n\nExit? ")
            else:
                playsound("/Users/erictyler/Turtle Racer/Failure.mp3", False)
                tk.messagebox.askyesno(title="YOU LOSE", message=f"You lose😭😭😭 {winner} was the winning turtle\n\nPlease call 1-800-GAMBLER (426-2537) to seek free, confidential, 24/7 problem gambling assistance\n\nExit? ")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


