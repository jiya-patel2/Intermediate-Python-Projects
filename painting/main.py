import turtle as t
import colorgram as c
import random as r
t.colormode(255)
# colors = c.extract('images.png',20)
# rgb_colors= []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

colors = [
    (236, 225, 81),
    (202, 6, 72),
    (235, 50, 129),
    (197, 165, 9),
    (207, 76, 12),
    (110, 178, 216),
    (222, 161, 99),
    (235, 224, 6),
    (31, 188, 108),
    (23, 106, 173),
    (18, 28, 175),
    (214, 135, 176),
    (13, 24, 65),
    (119, 186, 215),
    (229, 167, 198),
    (205, 28, 143)
]

tim = t.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
def left():
    for i in range(10):
        tim.pendown()
        tim.dot(20,r.choice(colors))
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)

def right():
    for i in range(10):
        tim.forward(50)
        tim.pendown()
        tim.dot(20, r.choice(colors))
        tim.penup()
    tim.right(90)
    tim.forward(50)
    tim.right(90)


for i in range(5):
    left()
    right()

tim.speed("fastest")




screen = t.Screen()
screen.exitonclick()