from turtle import Turtle
from ship_laser import ShipLaser

PIXELS = [{"x": 6, "y": 0},

          {"x": 5, "y": 1},
          {"x": 6, "y": 1},
          {"x": 7, "y": 1},

          {"x": 5, "y": 2},
          {"x": 6, "y": 2},
          {"x": 7, "y": 2},

          {"x": 1, "y": 3},
          {"x": 2, "y": 3},
          {"x": 3, "y": 3},
          {"x": 4, "y": 3},
          {"x": 5, "y": 3},
          {"x": 6, "y": 3},
          {"x": 7, "y": 3},
          {"x": 8, "y": 3},
          {"x": 9, "y": 3},
          {"x": 10, "y": 3},
          {"x": 11, "y": 3},

          {"x": 0, "y": 4},
          {"x": 1, "y": 4},
          {"x": 2, "y": 4},
          {"x": 3, "y": 4},
          {"x": 4, "y": 4},
          {"x": 5, "y": 4},
          {"x": 6, "y": 4},
          {"x": 7, "y": 4},
          {"x": 8, "y": 4},
          {"x": 9, "y": 4},
          {"x": 10, "y": 4},
          {"x": 11, "y": 4},
          {"x": 12, "y": 4},

          {"x": 0, "y": 5},
          {"x": 1, "y": 5},
          {"x": 2, "y": 5},
          {"x": 3, "y": 5},
          {"x": 4, "y": 5},
          {"x": 5, "y": 5},
          {"x": 6, "y": 5},
          {"x": 7, "y": 5},
          {"x": 8, "y": 5},
          {"x": 9, "y": 5},
          {"x": 10, "y": 5},
          {"x": 11, "y": 5},
          {"x": 12, "y": 5},

          {"x": 0, "y": 6},
          {"x": 1, "y": 6},
          {"x": 2, "y": 6},
          {"x": 3, "y": 6},
          {"x": 4, "y": 6},
          {"x": 5, "y": 6},
          {"x": 6, "y": 6},
          {"x": 7, "y": 6},
          {"x": 8, "y": 6},
          {"x": 9, "y": 6},
          {"x": 10, "y": 6},
          {"x": 11, "y": 6},
          {"x": 12, "y": 6},

          {"x": 0, "y": 7},
          {"x": 1, "y": 7},
          {"x": 2, "y": 7},
          {"x": 3, "y": 7},
          {"x": 4, "y": 7},
          {"x": 5, "y": 7},
          {"x": 6, "y": 7},
          {"x": 7, "y": 7},
          {"x": 8, "y": 7},
          {"x": 9, "y": 7},
          {"x": 10, "y": 7},
          {"x": 11, "y": 7},
          {"x": 12, "y": 7},]

start_position = {"x": -5*6, "y": -350}

class Ship:
    def __init__(self):
        self.center = {"x": start_position["x"] + 5 * 5,
                       "y": start_position["y"] - 5 * 4}
        self.dots = []
        self.step = 8
        for coordinate in PIXELS:
            dot = Turtle()
            dot.shape("square")
            dot.color("black")
            dot.penup()
            dot.shapesize(stretch_len=0.2, stretch_wid=0.2)
            x = start_position["x"] + coordinate["x"] * 5
            y = start_position["y"] - coordinate["y"] * 5
            dot.goto((x, y))
            self.dots.append(dot)

        self.lasers = []

    def move_right(self):
        self.center["x"] += self.step
        for dot in self.dots:
            x = dot.xcor() + self.step
            dot.goto((x, dot.ycor()))

    def move_left(self):
        self.center["x"] -= self.step
        for dot in self.dots:
            x = dot.xcor() - self.step
            dot.goto((x, dot.ycor()))

    def shoot(self):
        if len(self.lasers) < 5:
            laser = ShipLaser(self.center)
            self.lasers.append(laser)