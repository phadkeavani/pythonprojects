import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
DOT_SIZE = 20
ROWS = 10
COLUMNS = 10
colors = [(157, 15, 23), (117, 167, 188), (30, 110, 158), (234, 83, 44), (124, 175, 145), (7, 98, 38), (172, 20, 15), (30, 130, 48), (182, 185, 27),
          (200, 63, 27), (11, 42, 76), (16, 62, 41), (238, 202, 8), (136, 83, 96), (91, 15, 25), (49, 166, 77), (37, 27, 23), (176, 135, 148), (6, 66, 137), (50, 151, 196), (215, 67, 72),
          (232, 169, 161), (167, 208, 174), (78, 133, 185), (228, 168, 172), (176, 190, 215), (161, 203, 215), (32, 75, 84), (67, 64, 58), (247, 12, 14)]

def draw_dot():
    tim.pendown()
    tim.dot(DOT_SIZE, random.choice(colors))

def take_step_forward():
    tim.penup()
    tim.forward(DOT_SIZE + 10)

def move_to_next_line():
    tim.left(90)
    take_step_forward()
    tim.left(90)
    for b in range(COLUMNS):
        take_step_forward()
    tim.left(180)

# color_list = colorgram.extract('image.jpg', 100)

# for c in color_list:
#     c_tuple = (c.rgb.r,c.rgb.g,c.rgb.b)
#     colors.append(c_tuple)
# print(colors)
scr = Screen()
tim = Turtle()
tim.shape("circle")
tim.color("white")

for r in range(ROWS):
    for c in range(COLUMNS):
        draw_dot()
        take_step_forward()
    move_to_next_line()

scr.exitonclick()