#Thank you to Michael and Linux Magazine for the code I've been following :)

#all the beginning stuff


#this clears the screen
import os,sys
def ClearScreen():
	os.system('cls' if os.name=='nt' else 'clear')
ClearScreen()

#imports the random module
from random import *

#the title screen
def title():
	print ("     _____     __       ")
	print ("    /  ___|   /  \      ")
	print ("    | |  __  / /\ \     ")
	print ("    | |_| | / /  \ \    ")
	print ("     Good Adventure     ")
	print (" By Quantum Corporation  ")       
	print
title()

#setting up stats
MH = 10
HP = 10
DP = 1
MP = 1
SP = 1
AP = 2
gameOver  = 0

#you can get different stats for different names
name      = raw_input("What's your name? ")
if name == "Max":
	print ("You're just plain stupid.")
	MH = 5
	HP = 5
	DP = 0
	MP = 0
	SP = 0
	AP = 1
elif name == "Gabe":
	print ("You win.")
	MH = 100
	HP = 100
	AP = 10
	DP = 10
	MP = 10
	SP = 10
else:
	print ("Nice to meet you, " + name)

#so they know what to do
print ("Hint- type in help for help")
print




#all the commands


#help menu
def help():
	print
	print (" Help ")
	print ("======")
	print ("help")
	print ("stats")
	print ("exit")
	print ("fight")
	print ("clear")

#displays your stats
def stats():
	print
	print ("    Stats ")
	print ("==============")
	print ("Health : " + str(HP) + "/" + str(MH))
	print ("Attack : " + str(AP))
	print ("Defense: " + str(DP))
	print ("Magic  : " + str(MP))
	print ("Speed  : " + str(SP))

#fight
def fight():
	global HP
 	enemyhealth  = randint(6,12)
        enemyattack  = randint(1,3)
        enemydefense = 1
	print ("You see a troll. Its stats are:")
	print ("Health : " + str(enemyhealth) + "/" + str(enemyhealth))
	print ("Attack : " + str(enemyattack))
	print ("Defense: " + str(enemydefense))
	troll = raw_input("What do you do? ")
	HP = HP - enemyattack

#easter egg
def easteregg():
	print ("The developers probably told you how to find this easter egg.")
	print ("Good job anyway.")
	print ("Achievement: do what the developers tell you.")

#sets gameOver to 1 so you can leave the game
def exit():
	global gameOver
	gameOver = 1







#all the stuff keeping the game going


#interprets the commands
def interpret(command ):
	if (command == "stats"):
		stats()
	elif (command == "help"):
		help()
	elif (command == "stats"):
		stats()
	elif (command == "exit"):
		exit()
	elif (command == "fight"):
		fight()
	elif (command == "clear"):
		ClearScreen()
	elif (command == "easter egg"):
		easteregg()
	else:
		print ("English, please.")

#core game loop. takes input and sends you to command interpreter
while (gameOver == 0):
	print
	interpret(raw_input(name + "-> "))






#finishing stuff


#closing statements
ClearScreen()
