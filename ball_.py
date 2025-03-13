
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10 # Horizontal movement speed
        self.y_move = 10 # Vertical movement speed
        self.move_speed = 0.1 # Control ball speed
    
    def move(self):
        """Move the ball to a new position based on its current direction."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the vertical direction of the ball."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the horizontal direction of the ball and increase its speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball to the center and restore its speed."""
        self.goto(0, 0)
        self.move_speed = 0.1 # Reset speed to initial value
        self.bounce_x() # Change direction to avoid immediate repetition

