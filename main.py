from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


screen.listen()

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
