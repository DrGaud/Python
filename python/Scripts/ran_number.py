#print random lottery numbers

import random

"""
Make two lists
One is a random number list with a maximum of 6 numbers
Second list is 2 numbers randomly generated.
"""
lotto = range(0,52)
print lotto

def num_gen():
	gen = random.randint(1,51)
	return gen
	
	




ball1 = num_gen()
ball2 = num_gen()
ball3 = num_gen()
ball4 = num_gen()
ball5 = num_gen()
ball6 = num_gen()

	
print ball1
print ball2
print ball3
print ball4
print ball5
print ball6

list = []
list.append(ball1)
list.append(ball2)
list.append(ball3)
list.append(ball4)
list.append(ball5)
list.append(ball6)

print list.sort()


