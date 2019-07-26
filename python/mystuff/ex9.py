#Printing, Printing, Printing
#Some strange stuff in this exercise...

#This part shows how to display a string as a horizontal list
days = "Mon Tue Wed Thu Fri Sat Sun"
#This next 'trick' ' \n...' allows for the string to be split into new lines 
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#This is the call function
print "Here are the days: ", days
print "Here are the months: ", months

#This next part is very interesting, by using the """ allows you to write paragraphs
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, 
or 5, 
or 6...
..
%s
%s
""" % (days , months)