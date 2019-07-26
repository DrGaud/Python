#Understanding the Yield Function

mygen = (x*x for x in range (3))

for i in mygen:
	print "This is running throught he iterations where x*x three times", i

def createGen():
	mylist = range(3)
	for i in mylist:
		yield i

mygen = createGen()
print "This will print with yeild",(mygen)

for i in mygen:
	print "This prints out the iterations", (i)
	