# Functions can return something

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def sub(a, b):
	print "SUBTRACTING %d - %d" % ( a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLY %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDE %d / %d" % (a, b)
	return a / b

print "Lets do some math with just the functions"

age = add(float(raw_input("Enter Value: ")), float(raw_input("Enter Value: ")))
height = sub(float(raw_input("Enter Value")), float(raw_input("Enter Value")))
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: {0}, Height:{1}, Weight: {2}, IQ:{3}" .format(age, height, weight, iq)

#puzzel for extra credit

print "\nHere is a puzzle for you"

what = add(age, sub(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do that by hand"

whatif = add(age, multiply(height, divide(height, weight)))

print "If what is: ", what, "then whatif is: ", whatif, 