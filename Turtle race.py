'''Hey all ...The following is a simple python program which deals with the concept of turtle race..The code mainly uses turtle module and its basic functions thus gives an understanding of the respected module and its operations..
I do recommend to revise your concept of graphs in mathematics before starting this project
Hope you will give a good time while dealing with this...'''

#Importing necessary modules
import random
import turtle
from turtle import Turtle,Screen

#Screen
s1 = Screen()
WIDTH = 500 # X coordinate
HEIGHT = WIDTH # Y coordinate

#Screen setup
s1.setup(WIDTH,HEIGHT)

def turtle_count():
	while True:
		try:
			count = int(input('How many turtles you want?(Enter a number between 2-10): '))
		except(ValueError):
			print('Invalid Input')
		else:
			if 2 <= count <=10:
				return count
			else:
				print('Input is of invalid range..!Enter again..')

def ground():
	ground = Turtle()
	ground.hideturtle()
	ground.penup()
	#Turtle initially stays at the point (0,0)
	ground.goto(-WIDTH//2,HEIGHT//2)
	
	for i in range(4):
		ground.pendown()
		ground.forward(HEIGHT)
		ground.right(90)

def track(count):
	#n turtles means n+1 spaces 
	x_spacing = WIDTH//(count+1)
	
	for i in range(1,count+1):
		new_turtle = Turtle()
		new_turtle.penup()
		new_turtle.shape('turtle')
		new_turtle.color('black')
		new_turtle.hideturtle()
		new_turtle.left(90)
		
		#Drawing thevtrack
		new_turtle.goto(((-WIDTH//2) + (x_spacing * i)),-HEIGHT//2)
		new_turtle.pendown()
		new_turtle.forward(WIDTH)
		
def finish_line():#Draw the finish line
	line = Turtle()
	line.hideturtle()
	line.penup()
	line.color('red')
	line.goto((-WIDTH//2),(HEIGHT-20)//2)
	line.pendown()
	line.forward(WIDTH)
	
def racing_turtles(count):
	
	turtle_list = []
	colors = ["black", "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta", "gray", "lightgray", "darkgray"]
	
	#n turtles means n+1 spaces(Count the number of spaces between the turtles and between the turtle and the border)
	x_spacing = WIDTH//(count+1)
	
	for i in range(1,count+1):
		new_turtle = Turtle()
		new_turtle.shape('turtle')
		new_turtle.color(colors[i])
		new_turtle.left(90)
		new_turtle.penup()
		new_turtle.goto(((-WIDTH//2) + (x_spacing * i)),-HEIGHT//2)
		turtle_list.append(new_turtle)
	
	return turtle_list	

def race():	
	#Pen 
	pen = Turtle()
	pen.hideturtle()
	pen.penup()
	pen.goto(-100,0)
	pen.pendown()
	
	print('The turtle which touches the Red line first wins....!')
	#count = turtle_count()
	count = 5
	ground()#Draw the ground
	track(count)#Draw the track
	finish_line()#Draw the finish line
	list = racing_turtles(count)#Getting the Racing turtles
	
	flag = 0
	while flag == 0:
		for i in list:
			range = random.randrange(2,10)
			i.forward(range)
			if i.ycor() >= (HEIGHT//2)- 20:
				win = i.pencolor().title()
				pen.color(i.pencolor())		
				pen.write(f'{win} Wins', font=("Arial", 5, "normal"))
				flag = 1
				
				break

race()
s1.mainloop()