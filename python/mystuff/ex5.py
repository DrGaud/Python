# More variables and Printing

my_name = 'Pete'
my_age = 32
my_height = 182 #cm
my_weight = 83 #kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg in weight." % my_weight
print "Which isnt that heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
#this line can be written another way.
print "If I re-write this like {0},{1},{2}, I would get %d" .format(my_age, my_height, my_weight) % (my_age+my_height+my_weight)#Note to do the Sum in the string, the string formatter was used % not the .formatter {}method
