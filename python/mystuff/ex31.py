#Making Decisions

print "You enter a dark room with two doors. DO you go through #1 or #2 ?"

door = int(raw_input("> "))

#This is a function to test if the raw_input is within range
def int_test(x):
	if door == range (1,3):
		return
	else:
		print "Please enter a number between %d & %d" % (1,3)

int_test(door)

	
if door == 1 :
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1: Take the cake."
	print "2: Scream like a sissy at the bear."
	
	bear = int(raw_input("> "))
	
	if bear == 1:
		print "The bear eats your face off. Good job!"
	elif bear == 2:
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == 2:
	print "You stare into the endless abyss that is Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow Jacket clothespins."
	print "3. Purple monkey dishwasher!"
	
	insanity = int(raw_input("> "))
	
	if insanity == 1 or insanity == 2 :
		print "Your body survivies powered by a mind of Jello. Good Job!"
	else:
		print "The insanity rots your eyes into a pool of goo. Good Job!"
#This is a range test to make sure that the right input was given.
elif int_test != range(1,3):
	print "Just die now"
else:
	print "You stumble around and fall on a knife and die. Good Job!"

