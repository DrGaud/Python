#While Loops

"""A While loop will keep executing code if the boolean expression is True. It is a simple If-Statement but instead of running a block of code once if True, it would keep running through the block untill it reaches the first False expression.
The issue with while-loops is that they sometimes dont stop. They can keep going on forever. 
To avoid this issue follow the following rules:
1) Make sure that you use While-loops sparingly. For loops are always better!
2) Review the while loops to make sure the logic behind it will produce a false expression at one point.
3)when in doubt print out a test varible at the top and bottom of the while-loop to see what it's doing 
"""
i = 0
numbers = []

#This is saying while i equal to values less than 6 print keep doing the block of code.
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)#Here we are adding to the list for every iteratation
	
	
	i = i + 1 #This is a strange one, telling to change the i varible by taking the current value and adding its new value for the iteration to itself. probably could be written as i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "


for num in numbers:
	print num