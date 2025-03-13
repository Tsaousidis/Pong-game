
from turtle import Screen, Turtle
from paddle import Paddle
from ball_ import Ball
from scoreboard import Scoreboard
import time

def main():
    # Initialize the game screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0) # Disable automatic screen updates for smoother animation
    screen.textinput("Pong", "Press ENTER to start") # Display a start prompt

    # Create game objects
    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball() 
    scoreboard = Scoreboard()

    # Listen for key presses to move paddles
    screen.listen()
    screen.onkeypress(right_paddle.go_up, "Up")
    screen.onkeypress(right_paddle.go_down, "Down")
    screen.onkeypress(left_paddle.go_up, "w")
    screen.onkeypress(left_paddle.go_down, "s")  
    
          

    game_over = False
    while not game_over:
        time.sleep(ball.move_speed) # Control ball speed
        screen.update()  # Refresh screen manually
        ball.move() # Move the ball

        # Detect collision with the top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
            
        # Detect collision with paddles
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            
        # Detect when right paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.left_point()

        # Detect when left paddle misses
        if ball.xcor() < -380:
            ball.reset_position() 
            scoreboard.right_point() 

        # End the game when a player reaches 10 points
        if scoreboard.left_score == 10:
            game_over = True
            print("Left player won!")      
        elif scoreboard.right_score == 10:
            game_over = True
            print("Right player won!")     

    screen.exitonclick() # Keep the window open until clicked


if __name__ == "__main__":
    main() # Start the game