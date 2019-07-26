# Asking Questions

print "How old are you?",
age = raw_input("Enter Age")#Here I entered in a prompt within the raw_input() function
print "How tall are you?",
height = raw_input ("Enter Height")
print "How much do you weigh,",
weight = raw_input("Enter Weight")


print "So, you're %r old, %r tall and %r heavy." % ( age, height, weight) #here the formatter calls in the results from the raw_input function
