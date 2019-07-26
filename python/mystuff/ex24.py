# Ex24- More Python Practicing

#Here we are using the escape \\ commands int eh print statement.
print "Let's practice everything."
print "You\'d need to know \'bout dealing with \\escape statements\\ that do \n newlines and \t tabs"

#Here we have made the poem a multilined print statement
poem = """
\tThe lovely world
with logic so firmly planted
cannot dicern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

#Here we are outputing the varible poem as a call funtion to print
print "--------------------"
print poem
print "--------------------"

#Here a varible is calculating the math of the varible and calling it into the print statement
five = 10 - 2 + 3- 6
print "this should be five: %s" % five

#Here we are defining a function with variables set to return the values of their respective arguements.
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#Here we are introducing values to the function
start_point = 1000 #tbh we could do a raw_input to get the user to enter the value here
beans, jars, crates = secret_formula(start_point) # beans and jelly_beans are synonomis with each other, the varible inside the function is temporary, when it is returned in the function it can be called assigned to a varible for later, here beans just holds the value for jelly_beans

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)

start_point = start_point /10
print "We can also do that this way: "
print "We'd have %d beans, %d Jars, and %d crates" % secret_formula(start_point)# I tried to use {} tuples to enter the arguements into the statement, however was given IndexError: tuple index out of range. This is probalby down to the fact the arguements being called is stored within the function. idk
