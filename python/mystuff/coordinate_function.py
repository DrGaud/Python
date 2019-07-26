class coordinate(object):
	#Defining an __init__ method where the x,y are passed to the self attribute
	def __init__(self, x, y):
		self.x = x
		self.y = y
	#defining a distance method to calculate the distance between two points
	def distance (self, other):
		x_diff_sq = (self.x - other.x)**2
		y_diff_sq = (self.x - other.y)**2
		return int((x_diff_sq + y_diff_sq)**0.5)

print "Please enter in new coordinates:"
a = int(raw_input("X:>"))
b = int(raw_input("Y:>"))
c = coordinate (a,b)
origin = coordinate (0,0)
print "Coordinates are x:{0} y:{1}" .format(c.x ,c.y)
print "Origin is: x:{0} y:{1} " .format(origin.x, origin.y)
print c.distance(origin)
