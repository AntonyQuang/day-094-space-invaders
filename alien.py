from turtle import Turtle

# Pixels to draw the space invader
PIXELS = [{"x": 3, "y": 0},
          {"x": 9, "y": 0},

          {"x": 4, "y": 1},
          {"x": 8, "y": 1},

          {"x": 3, "y": 2},
          {"x": 4, "y": 2},
          {"x": 5, "y": 2},
          {"x": 6, "y": 2},
          {"x": 7, "y": 2},
          {"x": 8, "y": 2},
          {"x": 9, "y": 2},
          {"x": 2, "y": 3},
          {"x": 3, "y": 3},
          {"x": 5, "y": 3},
          {"x": 6, "y": 3},
          {"x": 7, "y": 3},
          {"x": 9, "y": 3},
          {"x": 10, "y": 3},

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

          {"x": 1, "y": 5},
          {"x": 3, "y": 5},
          {"x": 4, "y": 5},
          {"x": 5, "y": 5},
          {"x": 6, "y": 5},
          {"x": 7, "y": 5},
          {"x": 8, "y": 5},
          {"x": 9, "y": 5},
          {"x": 11, "y": 5},

          {"x": 1, "y": 6},
          {"x": 3, "y": 6},
          {"x": 9, "y": 6},
          {"x": 11, "y": 6},

          {"x": 4, "y": 7},
          {"x": 5, "y": 7},
          {"x": 7, "y": 7},
          {"x": 8, "y": 7},

          ]


class Alien:
    def __init__(self, start_position):
        self.dots = []
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

    def move_right(self):
        for dot in self.dots:
            step = 5
            x = dot.xcor() + step
            dot.goto((x, dot.ycor()))

    def move_left(self):
        for dot in self.dots:
            step = 5
            x = dot.xcor() - step
            dot.goto((x, dot.ycor()))

    def move_down(self):
        for dot in self.dots:
            step = 5
            y = dot.ycor() - step
            dot.goto((dot.xcor(), y))