#Strings and Text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: %s." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#This part of the print statement calls in the string frrom the varible-hilarious into the print statement
print joke_evaluation % hilarious

w = "This is the left side of a ..."
e = "This is the right side of the string."

print w + e #This is the left side of a ... this is a right ...
#The above statement can also be expressed as a comma to link the two strings together
print w , e
print w e 
