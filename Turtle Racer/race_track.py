from turtle import *


def draw_track():
    penup()
    goto(0, 200)
    pendown()
    write("🏁🐢TURTLE RACERS🐢🏁", align="center", font=("Arial", 24, "bold"))
    #dirt
    penup()
    goto(-350, 200)
    pendown()
    color("chocolate4")
    begin_fill()
    for i in range(2):
        forward(700)
        right(90)
        forward(400)
        right(90)
    end_fill()


    #finishline
    gap_size = 20
    shape("square")
    penup()

    # WHITE SQUARES ROW 1
    color("white")
    for i in range(10):
        goto(250, (170 - (i * gap_size * 2)))
        stamp()

    # WHITE SQUARES ROW 2
    for i in range(10):
        goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
        stamp()

    # BLACK SQUARES ROW 1
    color("black")
    for i in range(10):
        goto(250, (190 - (i * gap_size * 2)))
        stamp()

    # BLACK SQUARES ROW 2
    for i in range(10):
        goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
        stamp()


def celebrate():
    speed(100)
    setheading(270)
    forward(10)
    for i in range(50):
        left(10)
        forward(1)