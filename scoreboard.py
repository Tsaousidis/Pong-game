
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard() # Display initial scoreboard

    def update_scoreboard(self):
        """Clear and redraw the scoreboard with updated scores."""        
        self.clear()
        self.goto(-100, 200) # Position for left player's score
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200) # Position for right player's score
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        """Increase left player's score and update the scoreboard."""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """Increase right player's score and update the scoreboard."""
        self.right_score += 1
        self.update_scoreboard()