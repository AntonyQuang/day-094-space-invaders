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
    x = top_left_xcor + 70*i
    for j in range(5):
        y = top_left_ycor - 70*j
        start_position = {"x": x,
                          "y": y,
                          }
        aliens.append(Alien(start_position))

left_wall_xcor = -450
right_wall_xcor = 450

screen.update()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for alien in aliens:
        for dot in alien.dots:
            if dot.xcor() >= right_wall_xcor or dot.xcor() <= left_wall_xcor:
                for alien in aliens:
                    alien.bounce()
        alien.move()



screen.exitonclick()