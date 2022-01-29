
from turtle import Turtle

class score(Turtle):
	def __init__(self):
		super().__init__()
		self.color("White")
		self.penup()
		self.hideturtle()
		self.player1_score = 0
		self.player2_score = 0
		self.update_score()
	def update_score( self ): #resets the scores by adding another turtle towards it thus stacking turtle scores
		self.clear() #will clear the screen of all scores
		self.goto(-200 , 200)
		self.write(f"P1 Score: {self.player1_score}" , align="center" , font=("Courier" , 20 , "normal"))
		self.goto(200 , 200)
		self.write(f"P2 Score: {self.player2_score}" , align="center" , font=("Courier" , 20 , "normal"))
	def p1_point( self ): # add scores
		self.player1_score += 1
		self.update_score()
	def p2_point( self ):
		self.player2_score += 1
		self.update_score()



