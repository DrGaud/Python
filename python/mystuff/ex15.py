#Reading Files
#This takes in arguments from the command line and imports it into the script
from sys import argv

#Here the variables are set and declared by argv
script, filename = argv

#This open() command allows the script to open a file with the corresponding file name
txt = open(filename)

#This allows for the name of the file to be repersented in its raw format, if it was done by a string it would have a problem deciphering it.
print "Here's your file %r:" % filename
#This prints out the contents of the document by using the Fileobject.read() function
print txt.read(),
#Here we use the close function to close the file that is open. Fileobject.close()
txt.close()

#This is where the raw_input funtion is used where the argument is passed directly into the script by the user
print "Type the filename again:"
#Here we are setting the varible file_again with a raw_input entry
file_again = raw_input("> ")

#This allows for the varible txt to open the file determined by the raw_input function 
txt_again = open(file_again)
#This prints/reads the file defined by file_again, 
print txt_again.read()
#Here we are closing the file with the Fileobject.close()
txt_again.close()
