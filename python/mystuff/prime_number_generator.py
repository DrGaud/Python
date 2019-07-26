""" This is a script to generate prime numbers from a range of numbers.
Or by checking to see if the input number is prime.
"""

#Calculate the prime numbers between two numbers
#Allow the user to enter in a range of numbers
#Secondly be able to have the user enter a number to check to see if it is prime
#thirdly have the user able to choose at the start which test they wish to be running.
#be able to restart the script or quit based on user input

#Calculating the prime numbers between two numbers

user_input1 = int(raw_input("Please enter value here: "))
user_input2 = int(raw_input("Please enter value here: ")) 
user_input3 = int(raw_input("> "))
user_input_intro= int(raw_input("> "))





print "What would you like to test."
print "1: Test a number to see if it is prime?"
print "2: Calculate the prime numbers between two numbers?"
	
choice = user_input_intro

if choice == 1:
	return isprime
elif choice == 2:
	return prime_r
else:
	print "Sorry Please enter in a number between 1 and 2."


def isprime(num):
	print "What number do you think is prime?"
	num = user_input3
	if num % num == 0 and num / num == 1:
		print "{} is a Prime Number." .format(num)
	else:
		print "Sorry but {} is not a Prime number" . format(num)
		
def prime_r(num1,num2):
	print "Please enter the starting value here:"
	num1 = user_input1
	print "Please enter the last number here:"
	num2 = user_input2
	for num in range(num1, num2):
		for i in range (2, num2):
			if num % i == 0: # If number is wholely divisible by 1 or itself equal to zero. then ture. 
				j= num / i
				print "{0} equals {1} * {2}" .format(num,i,j)
				break
	else:
		print num, "is a Prime Number"