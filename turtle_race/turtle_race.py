from turtle import Turtle,Screen
import random
race_is_on = False
scr = Screen()
scr.setup(width=500, height=400)
scr.register_shape("finish_flag.gif")

colors = ["red", "orange","yellow","green","blue","indigo", "violet"]
turtles = []
flag_turtle = Turtle(shape="finish_flag.gif")
flag_turtle.shapesize(1.0, 1.0, 1)
flag_turtle.hideturtle()
flag_turtle.penup()
flag_turtle.setposition(230,0)


for i in range(7):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    if i == 0:
        y = 0
    elif i % 2 == 0:
        y = i * 20
    else:
        y = (i + 1) * -20
    t.goto(-230, y)
    turtles.append(t)

user_bet = scr.textinput(title='Make a guess', prompt='Which turtle will win the race? Enter color: ')

if user_bet is not None and user_bet in user_bet:
    race_is_on = True

while race_is_on:
    step_length = random.randint(0,10)
    timmy = random.choice(turtles)
    y = timmy.ycor()
    if timmy.distance(230, y) < 100:
        flag_turtle.setposition(230, y)
        flag_turtle.showturtle()
    if timmy.distance(230, y) < 10:
        step_length = timmy.distance(230, y)

    timmy.forward(step_length)

    if timmy.xcor() == 230:
        race_is_on = False
        if user_bet == timmy.fillcolor():
            print(f"You won! {timmy.fillcolor()} turtle won the race")
        else:
            print(f"You lose! {timmy.fillcolor()} turtle won the race")



scr.exitonclick()