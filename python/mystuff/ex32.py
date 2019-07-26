#Ex32 Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

#This is first kind of for-loop goes through a list
for number in the_count:
	print "This is the count {}" .format(number)
	
#same as above
for fruit in fruits:
	print "A fruit of type: {}" .format(fruit)

#We can also go through mixed lists too

for i in change:
	print "I got {}" .format(i)

#We can also build lists, by starting with an empty one

elements = []

#Then use the range function to do a 0 to 5 count
for i in range (0,6):
	print "Adding {} to the list." .format(i)
	#append is a function that lists understands
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Element was: {}" .format(i)


for num in range(10, 20):#For every number in the range 10-19
	for i in range(2, num): # i = range between 2 and number from above...
		if num % i == 0: # If number is wholely divisible by 1 or itself equal to zero. then ture. 
			j= num / i
			print "{0} equals {1} * {2}" .format(num,i,j)
			break
	else:
		print num, "is a Prime Number"



