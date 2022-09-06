import turtle
import time
from alien import Alien

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.title("Space Invaders")
# Turn off delay in animations
screen.tracer(0)


# putting the aliens on the
aliens = []
start_positions = []

top_left_xcor = -400
top_left_ycor = 300

for i in range(8):
    x = top_left_xcor + 80*i
    for j in range(6):
        y = top_left_ycor - 55*j
        start_position = {"x": x,
                          "y": y,
                          }
        aliens.append(Alien(start_position))

left_wall_xcor = -430
right_wall_xcor = 400

screen.update()


game_is_on = True
direction = "right"
previous_direction = direction

while game_is_on:
    for alien in aliens:
        if alien.center["x"] >= right_wall_xcor:
            direction = "left"
        elif alien.center["x"] <= left_wall_xcor:
            direction = "right"
    if previous_direction != direction:
        for alien in aliens:
            alien.descend()
        screen.update()
        time.sleep(0.1)
    if direction == "right":
        for alien in aliens:
            alien.move_right()
    else:
        for alien in aliens:
            alien.move_left()
    screen.update()
    time.sleep(0.1)
    previous_direction = direction



screen.exitonclick()