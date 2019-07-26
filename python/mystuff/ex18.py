#Names variables, Code and Functions

#This one is like the scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1 , arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
	print "arg1: {0}, arg2: {1}"  .format( arg1, arg2)

def print_one (arg1):
	print "arg1: {0}" .format(arg1)

def print_none ():
	print "I got noting'."


print_two ("Peter","Singh")
print_two_again ("Peter","Singh")
print_one ("First!")
print_none ()

