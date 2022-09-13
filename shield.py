from turtle import Turtle

PIXELS = [
    {"x": 1, "y": 0},
    {"x": 2, "y": 0},

    {"x": 0, "y": 1},
    {"x": 1, "y": 1},
    {"x": 2, "y": 1},
    {"x": 3, "y": 1},

    {"x": 0, "y": 2},
    {"x": 3, "y": 2},
         ]


class Shield:
    def __init__(self, start_position):
        self.dots = []
        for coordinate in PIXELS:
            dot = Turtle()
            dot.shape("square")
            dot.color("black")
            dot.penup()
            dot.shapesize(stretch_len=1.5, stretch_wid=1.5)
            x = start_position["x"] + coordinate["x"] * (20*1.5)
            y = start_position["y"] - coordinate["y"] * (20*1.5)
            dot.goto((x, y))
            self.dots.append(dot)

