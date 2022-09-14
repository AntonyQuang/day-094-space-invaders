from turtle import Turtle

# Pixels to draw the alien_laser.py
PIXELS = [{"x": 0, "y": 0},
          {"x": 0, "y": 1},
          {"x": 1, "y": 2},
          {"x": 1, "y": 3},
          {"x": 0, "y": 4},
          {"x": 0, "y": 5},
          ]

class AlienLaser:
    def __init__(self, start_position):
        self.dots = []
        self.step = 20
        self.status = "alive"
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

    def move(self):
        if self.status == "alive":
            for dot in self.dots:
                y = dot.ycor() - self.step
                if y > -450:
                    dot.goto(x=dot.xcor(), y=y)
                else:
                    self.remove()

    def remove(self):
        self.status = "dead"
        for dot in self.dots:
            dot.goto((0, -900))
            dot.hideturtle()

