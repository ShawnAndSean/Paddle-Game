import random
from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from score import score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.tracer(0)  # turn off animation

player1 = Paddle((-350 , 0))
player2 = Paddle((350 , 0))

ball = Ball()
score = score()

screen.listen()

screen.onkeypress(player1.go_up , "w")
screen.onkeypress(player1.go_down , "s")
screen.onkeypress(player2.go_up , "Up")
screen.onkeypress(player2.go_down , "Down")

is_game = True

while is_game:
	time.sleep(ball.move_speed)  # will have 0.1 delay
	screen.update()
	ball.move()
	if ball.ycor() > 280 or ball.ycor() < -280:
		# needs to bounce
		screen.update()  # continue animation
		ball.bounce_y()
	# detect collision with player2
	if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() <- 320:
		ball.bounce_x()
		# player 2
	if ball.xcor()>400:
		ball.reset()
		score.p1_point()
		#player 1
	if ball.xcor()<-400:
		score.p2_point()
		ball.reset()


