import turtle
import time
from alien import Alien
from ship import Ship
from shield import Shield

from random import randint


screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.title("Space Invaders")
# Turn off delay in animations
screen.tracer(0)


# putting the aliens on the screen
aliens = []
shields = []
start_positions = []

top_left_xcor = -400
top_left_ycor = 300
bottom_left_xcor = -350
bottom_left_ycor = -200

for i in range(8):
    x = top_left_xcor + 80*i
    for j in range(5):
        y = top_left_ycor - 55*j
        start_position = {"x": x,
                          "y": y,
                          }
        aliens.append(Alien(start_position))

for i in range(4):
    x = bottom_left_xcor + 200*i
    start_position = {"x": x,
                      "y": bottom_left_ycor}
    shields.append(Shield(start_position))

left_wall_xcor = -410
right_wall_xcor = 400

ship = Ship()


screen.update()


game_is_on = True
direction = "right"
previous_direction = direction
count = 0
count_max = 5
directions = ["right" for i in range(2*count_max)]

screen.listen()
screen.onkeypress(fun=ship.move_left, key="Left")
screen.onkeypress(fun=ship.move_right, key="Right")
screen.onkeypress(fun=ship.move_right, key="Right")
screen.onkeypress(fun=ship.shoot, key="space")

while game_is_on:
    time.sleep(0.001)

    # Checks if the aliens have hit a wall, and decides what the next alien direction should be
    for alien in aliens:
        if alien.center["x"] >= right_wall_xcor:
            direction = "left"
        elif alien.center["x"] <= left_wall_xcor:
            direction = "right"

        # alien shoots:
        if randint(0, 1500) == 1:
            alien.shoot()
        for laser in alien.lasers:
            laser.move()

    # Decides when the aliens descend
    directions.append(direction)
    directions.pop(0)

    # if previous_direction != direction:
    if "left" in directions and "right" in directions:
        time.sleep(0.5)
        for alien in aliens:
            alien.descend()
        directions = [direction for i in range(2*count_max)]
        count = 0


    # Moves the aliens

    if direction == "right":
        # count += 1
        # if count > count_max:
        #     count = 0
            for alien in aliens:
                alien.move_right()
    else:
        # count += 1
        # if count > count_max:
        #     count = 0
            for alien in aliens:
                alien.move_left()

    # shield collision detection

    for shield in shields:
        for shield_dot in shield.dots:
            for laser in ship.lasers:
                for laser_dot in laser.dots:
                    if shield_dot.distance(laser_dot) < 15:
                        laser.remove()
                        shield.remove(shield_dot)
            for alien in aliens:
                for laser in alien.lasers:
                    for laser_dot in laser.dots:
                        if shield_dot.distance(laser_dot) < 15:
                            laser.remove()
                            shield.remove(shield_dot)

    # alien ship detection
    for alien in aliens:
        for alien_dot in alien.dots:
            for laser in ship.lasers:
                for laser_dot in laser.dots:
                    if laser_dot.distance(alien_dot) < 10:
                        laser.remove()
                        alien.kill()

    # player ship detection
        for laser in alien.lasers:
            for laser_dot in laser.dots:
                for ship_dot in ship.dots:
                    if laser_dot.distance(ship_dot) < 10:
                        laser.remove()
                        ship.die()

    for laser in ship.lasers:
        laser.move()

    screen.update()
    # Remembers what direction it was going, so it can compare it in the next loop
    previous_direction = direction

screen.exitonclick()