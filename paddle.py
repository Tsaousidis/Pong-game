
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """Initialize the paddle at the given position."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Move the paddle up within screen boundaries."""
        if self.ycor() < 240: # Prevent paddle from going off-screen
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move the paddle down within screen boundaries."""
        if self.ycor() > -240: # Prevent paddle from going off-screen   
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)        