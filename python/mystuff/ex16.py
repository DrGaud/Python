#Reading and Writting files

#Importing from the commandline
from sys import argv

#Setting the variables
script, filename = argv


print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL+C (^C)."
print "If you do want that, hit RETURN"
#User input
raw_input("?")

print "Opening the file..."
#Defining the fileobject as 'target', command to open 'filename' the 'W' allows for the file to be written
target = open(filename, "w")

print "Truncating the file. Goodbye!"
#Here we are using the fileobject.truncate to delete the contents of the file
target.truncate()


print "Now I'm going to ask you for thee lines"

#Here we are reciving the new lines to put into the file, via raw_input
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these three lines into the file"
#Here we are using fileobject.write([content]) to the file
#It is awfully messy, soo I have closed it off
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)

#So this line has been taken from stackoverflow
#It uses the new string and formatting structure.
#Breaking it down the {} is a reference function, numbered litterally to the positial argument that is being specified
#.format(arg1,arg2,...) is where the inputs are formatted into a string and allowed for output.
target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))