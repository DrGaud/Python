#Else and If


#I changed the exercise
#Here I have asked for a user input int(raw_input()
people = int(raw_input("How many people are there: "))
cars = int(raw_input("How many cars do you have?"))
buses = int(raw_input("How many buses?"))

#Here I have set the max amount of travelers per vehicle
car_max = 4
buses_max = 50

#Here I calculated how many would fit per vehicle type
ppl_cars = int(people / car_max)
ppl_buses = int(people / buses_max)

#Here are the if statements
if ppl_cars < cars:
	print "We should take the cars"
elif ppl_buses < buses:
	print "We should take the bus."
else:
	print "Sod it"
if ppl_cars > ppl_buses:
	print "There is more people travelling by car, that is not enviromentally friendly"
elif ppl_buses > buses:
	"There is more people travelling than buses avalible"
else: "GDMIT"

"""This is the script used in the exercise"""
#If true, print statement
if cars > people:
	print "We should take the cars"
#Else if true, print statement
elif cars < people:
	print "We should not take the cars"
#If both tests are False, return
else: 
	print "We can't decide"

if buses > cars:
	print "We should take the bus"
elif buses < cars:
	print "We should just take the car"
else:
	print "We still can't decide"

#If true, print statement. Else print if False
if people > buses:
	print "Alright, we should just take the bus!"
else: 
	print "Fine, let's stay home then."

if people / cars >= cars:
	"We cant fit everyone in a car"
elif people / buses >= buses:
	"We cant fit everyone on the buses either"
else:
	print "There is just to many %d" % people
