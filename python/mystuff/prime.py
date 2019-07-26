#Prime number 

print "What would you like to do?"
print "1: Find out if a number is prime? "
print "2: see what numbers are prime within a range?"

""" Looking to make sure that the user input provides a response between 1 and 2."""
def int_test(x):
	if x == range (1,3):
		return
	else:
		print "Please Enter a number between 1 and 2"

"""Getting the user input """
choice = int(raw_input(">"))
int_test(choice)#Testing the choice provided between 1 & 2


if choice == 1 and not choice >= 2 :
	print "Please enter in a number to see if it is a prime number or not: "
	
	x = int(raw_input(">"))
	
	for y in range(2, x):
		if x % y == 0:
			z= x / y
			print "{} is  NOT a prime number!".format(x)
			break
		else:
			print "{} is a Prime Number!".format(x)
if choice == 2 :
	print "Please enter the range of numbers you wish to find:"
	
	num1 = int(raw_input("minimum value >"))
	
	num2 = int(raw_input("maximum value >"))
	
	for num in range(num1,num2):
		for i in range(2,num): 
			if num % i == 0:
				j= num / i 
				print '%d equals %d * %d' % (num,i,j)
				break 
	else:
		print num, 'is a prime number'