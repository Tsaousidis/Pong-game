
from turtle import Screen, Turtle
from paddle import Paddle
from ball_ import Ball
from scoreboard import Scoreboard
import time

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball() 
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")  
    
          

    game_over = False
    while not game_over:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
            
        # Detect collision with both paddles
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            
        # Detect when right_paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.left_point()

        # Detect when left_paddle misses
        if ball.xcor() < -380:
            ball.reset_position() 
            scoreboard.right_point()       

    screen.exitonclick()


if __name__ == "__main__":
    main()