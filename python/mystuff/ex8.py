# Printing Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing",
	"So I said goodnight."#This annoys me
)

#So this next part I had made a few mistakes, the most glaringly obvious 
#was forgetting the ' , ' at the end of each string, else the program 
#Thought it was just one sting, not 4 indvidual strings. 
print formatter % ( 
	"I typed the poem above.",
	"I found it quite dull.",
	"If I had my way.",
	"It would be very fun.",
)

