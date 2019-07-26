#ex36 - creating my own logic game
from sys import exit
import random

pick_up_box = False
sword = False

def search_area():
	if pick_up_box == True:
		print "So you decided to pick up the box, \nYou begin to inspect other areas\nDays go by and you come across nothing interesting"
	else:	
		print "As you walk away from the box on the ground, \nYou begin to inspect other areas\n Days go by and you come across nothing interesting"
	print "Then on your way back, you notice a strange object of to the distance."
	print "Walking closer you discover a Sword embedded in Stone. \n upon closer inspection a message on the pommel reads\n'The sword of Destiny'"
	print "Do you reach in to take the sword?: Y/N"
		
	input = raw_input(">:")
		
	if input == "N":
		dead ("Well all you did was walk around and look about,\nYou seen a strange box and a sword in the stone,\nYet you were not curious to even inquire. Your risk aversion has allowed someone else\n The chance to stumble on these tokens \n You are indeed a pussy.\n Now go away....")
		restart()
	elif input == "Y":
		print "It is all down to the roll of the dice...lets hope its EVEN"
		
		dice=random.randint(0,6)
		print "The gods above have rolled a", dice
		
		if dice % 2 == 0:
			print "You are indeed worthy!!"
			print "Power starts to flow through you....\nYou are the Master of the Universe!!!\nFOR YOU HAVE THE POWER!!!"
			sword = True
			pandora_open()
			
			
		elif dice % 2 != 0:
			print "Do you want to try again?"
				
			input = raw_input
				
			if input == "N":
				dead ("You are not worthy....\nThe power of the sword knows this\nIt burns you up.")
				restart()
				
			elif input == "Y":
				dice
				print "Second Time around!!!"
				print "It feels like a scence from Highlander!\n Lightening strikes the sword..."
				print "You feel electric"
				pandora_open()
			else:
				print "Please input a Y/N response."
		else:
			print "Please input a Y/N response."
	else:
		print "Please input a Y/n response."
			

def box_status():
	if pick_up_box == True:
		print "So you decided to pick up the box"
	else:
		print "You decided to leave the box on the ground and continue on with your journey"
	


def pandora_open():
	print "You have now picked up the box,\nIt starts calling out your name."
	print "It is asking you to open it..."
	print "Do you open it...?: Y/N"
	
	input = raw_input(">:")
	
	if input == "Y":
		print "You have opened Pandoras Box...\nA Sound so loud it leaves your ears ringing, cracks through the air.\n The light from the day, has been blocked out. "
		print ".........................."
		print "Darkness fill the world as it spews forth from the mouth of the box."
		print "What do you do?"
		print "Do you try and close the box"
		
		input = raw_input(">:")
		
		if input == "Y":
			print "It can't be closed!!!"
			print "Do you try again?"
			
			input = raw_input(">:")
			
			if input == "Y":
				
				print "You try again to close the box, but it tips onto itside revealing a small sticker"
				
				print " !!!WARNING!!!\nDO NOT OPEN \nOR ELSE THE WORLD WOULD END \nIf you have opened it, dont panic! \nYou need to have the Sword of destiny to close it"
				
				check_sword = sword
				
				if check_sword is True:
					print "Do you want to use the sword to close the box?: Y/N"
					
					input = raw_input(">:")
					
					if input == "Y":
						print "You stab the darkness with the pointy end. \nPlunging it deeper and deeper into the dark \n Untill it hits something solid."
						
						print "you let go of the sword and for a brief second everything goes quiet."
						
						print ".............."
						
						print "Then the darkness comes rushing back into the box \nLike a torrent it comes rushing in.\nKnocking you clear on your feet."
						
						dead ("You won, the sun is back, the birds are singing \n all is well")
						restart()
						
					else: 
						dead ("You had a chance to save the world!!!!\nYou collosial twat!")
						restart()
				else:
					dead("Great, you opened pandora's box without checking to see if there was anything else in the area...\nYOU TWAT\nNow the world would end, all because you didnt have the sword of destiny.")
					restart()
		elif input == "N":
			dead("WHAT ARE YOU DOING!!!\nThe world is going to end because of you!")
			restart()
		else:
			print "Please choose either a Y/N response."
		

		

def start_new_round():
	"""This is where the game begins based on a Yes repsonse to the start_game_prompt response"""
	print "Welcome to Pandora's labirynth \nHere you will play a game\nOne that will test your resolve and patience"
	print "............................"
	print "One day on your travels you came upon a box, just lying there in the middle of nowhere."
	print "The box is extremely old and carved with all manner of dark symbols and rune styled inchantments"
	print "It gives off a very eirie vibe...."
	print "Do you pick it up?: Y/N"
	
	input = raw_input(">:")#Enter user input Y/N
	
	if input == "Y":
		print "Okay now it is really starting to 'sing' to you...\nDo you want to continue to SEARCH the area or OPEN the box"
		
		input = raw_input(">:")
		
		if input == "OPEN" or "open":
			pandora_open()#Launches pandora's box is opened
		elif input == "SEARCH" or "search": 
			pick_up_box = True
			search_area()#Launches search_area 
		else:
			print "Please pick either OPEN or SEARCH"
	elif input == "N":
		pick_up_box = False
		search_area()#Launches search_area
	else: 
		print "Please pick a Y/N repsonse"


def start_game_prompt():
	"""The Start Game prompt, is where the introduction the the game is made."""
	print "Welcome to Pandora's Box"
	print "Its a simple game, to see if you can withstand the course of python"
	print "Would you like to start the game: Y/N ?"
	
	input = raw_input(":>")#This captures the user input Y/N
	
	"""This is the control flow for the User Input"""
	if input == "Y":
		start_new_round()
	elif input == "N":
		dead("Thanks for not really playing!")
		restart()
	else:
		print "Please enter a Y/N response:"
		input

def restart():
	print "Would you like to restart the game?: Y/N"
	
	input= raw_input(">:")
	
	if input == "Y" or "y":
		start_new_game()
	elif input == "N" or "n":
		exit()
	else:
		"Please input a Y/N response."

def dead(why):
	print why 
		
def start_new_game():
	start_game_prompt()

start_new_game()