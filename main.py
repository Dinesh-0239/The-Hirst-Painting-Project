from turtle import Turtle, colormode, Screen, title
from random import  choice

title("The Hirst Painting")
colormode(255)
colors_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19),
              (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164),
              (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]
draw = Turtle()
draw.hideturtle()
draw.penup()
draw.speed("fastest")
draw.setheading(225)
draw.forward(300)

for point in range(100):
    draw.setheading(0)
    draw.dot(20,choice(colors_list))
    draw.forward(50)

    if (point + 1) %10 ==0:
        draw.setheading(90)
        draw.forward(50)
        draw.setheading(180)
        draw.forward(500)



screen = Screen()
screen.exitonclick()
