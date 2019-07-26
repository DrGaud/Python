#This takes the prompt from the command line
from sys import argv
#This brings in the arguments to check the path of the directory and see if it exists: True/False
from os.path import exists

#Here we are setting the arguements
script, from_file, to_file = argv

#Setting the indata varible to hold the file as it is read
indata = open(from_file).read()

#Here we are putting the indata dircetly into the output file, 'w' to allow for writting of the file
out_file = open(to_file, 'w')
#Here we are going to be printing on the output a line that allows for a differentiation of the two files.
out_file.write ("This is a clone from the simplified copy" + "\n")
#To be honest we could scrap the previous line and just have the following two commands
out_file.write(indata)
out_file.close()

print "Alright nigga thats it done"

####IT FUCKING WORKS!!!!!###### 