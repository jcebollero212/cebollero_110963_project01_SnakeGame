from graphics import *
from time import sleep #add delay in the execution of a program
from random import random #creating random number for snake food locations

def setCoordinateValues(x,y):
	return x,y

def setSnakeLength(len_s):
	return len_s

def isGrowing(grow):
	if grow == 1:
		return True
	else:
		return False

def selected_key(key, direction_X, direction_Y, q):
	if(key == "w"): #goes up
		direction_X=0 
		if(direction_Y==1): #Eat yourself, causing you to loose. 
			q=0 
		direction_Y=-1

	if(key == "s"): # goes down
		direction_X=0
		if(direction_Y==-1):
			q=0
		direction_Y=1
	if(key == "d"): #goes right
		if(direction_X==-1):
			q=0
		direction_X=1
		direction_Y=0
	if(key == "a"): #goes left
		if(direction_X==1):
			q=0
		direction_X=-1
		direction_Y=0
	return direction_X,direction_Y,q


def play(q, speed, current_X, current_Y, snake_lenght, s, a, food_X, food_Y, points, snake_food, w, direction_X, direction_Y, grow):
	while(q==1): #Infinite loop until player looses
		sleep(speed)  
		direction_X,direction_Y,q = selected_key(w.checkKey(), direction_X, direction_Y, q) #Get input from keyboard

		current_X+=direction_X #Moving the snakes head on x direction
		current_Y+=direction_Y #Moving the snakes head on y direction
		if(current_X>49 or current_Y>49 or current_X<0 or current_Y<=0): #If you get out the prefixed window you will loose.
			q=0
		#Snakes new position
		for i in range(snake_lenght-1,-1,-1):
			s[i]=s[i-1] 
			if(s[i] == [current_X,current_Y]):
				q=0
			a[i].undraw() 
		if(current_X == food_X and current_Y == food_Y): #Undraw snake food once eaten
			snake_food.undraw() #Destroy eaten Snake Food
			grow=1 
			food_X=int(random()*50) #Random Snake Food Location
			food_Y=int(random()*50)
			snake_food=Rectangle(Point(food_X*10,food_Y*10),Point(food_X*10+10,food_Y*10+10)) 
			snake_food.setFill('red')
			snake_food.draw(w) #Draw the new snake food
		s[0]=[current_X,current_Y] #New snakes head position
		a[4].undraw() #Undraw the piece of the last piece of the tail
		for i in range(snake_lenght): 
			a[i]=Rectangle(Point((s[i][0])*10,s[i][1]*10),Point((s[i][0])*10+10,s[i][1]*10+10))
			a[i].setFill('blue')
			a[i].draw(w) 
		if(isGrowing(grow)): 
			snake_lenght+=1 
			points.setText("Points: "+str((snake_lenght-5)*1)) #Increase the points by 1
			speed*=0.95 #Increase the game speed when the snake grows
			s.append([]) #Create new spaces for the new snake body
			a.append([]) 
			a[snake_lenght-1]=Point(0,0) 
			a[snake_lenght-1].draw(w) 
			grow=0


def GUI(q, speed, current_X, current_Y, snake_lenght, s, a, food_X, food_Y, direction_X, direction_Y, grow):
	w=GraphWin('Snake Game!', 500, 500)
	w.setBackground(color_rgb(0, 0, 0,)) #Black background
	for i in range(snake_lenght): 
		s.append([current_X-i,current_Y]) #append method will make it increase by one.  
		a.append([]) #append method will make it increase by one. 
		a[i]=Rectangle(Point((current_X-i)*10,current_Y*10),Point((current_X-i)*10+10,current_Y*10+10)) 
		a[i].setFill('blue') #Snake color 
		a[i].draw(w) 
	points=Text(Point(250,10),"Points: "+str((setSnakeLength(snake_lenght-5))*1)) #points box
	points.draw(w)
	snake_food=Rectangle(Point(food_X*10,food_Y*10),Point(food_X*10+10,food_Y*10+10)) #Drawing the snakes apple
	snake_food.setFill('red') #Snake food color
	snake_food.draw(w)

	play(q, speed, current_X, current_Y, snake_lenght, s, a, food_X, food_Y, points, snake_food, w, direction_X, direction_Y, grow)
	w.close()


def game():
	while(1): #Creating an Infinite loop
		speed=0.1 
		current_X, current_Y = setCoordinateValues(20,20)
		snake_lenght = setSnakeLength(5)
		s, a = [], []
		direction_X, direction_Y = setCoordinateValues(1,0)
		food_X, food_Y = setCoordinateValues(3,18)
		grow, q = setCoordinateValues(0,1)

		GUI(q, speed, current_X, current_Y, snake_lenght, s, a, food_X, food_Y, direction_X, direction_Y, grow)

game()
