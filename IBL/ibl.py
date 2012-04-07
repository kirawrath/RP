
class IBL1:
	def __init__(self):
		pass

	def euclidian_dist(self, a,b):
		d=pow(sum(map(lambda a, b: pow(a-b, 2), a.pos, b.pos)), 0.5)
		return d

	def train(self,dots):
		self.DC=[]
		hit=0; miss=0
		for d in dots:
			nearest = float('inf')
			nearest_dot = dots[0]
			for dc in self.DC:
				dist = self.euclidian_dist(d,dc)
				if dist < nearest:
					nearest = dist
					nearest_dot = dc
			if nearest_dot.clas == d.clas:
				hit += 1
			else:
				miss += 1
			self.DC.append(d)
		return (self.DC, hit, miss)


	def classify_test(self,dots):
		pass
	def classify(self,dots):
		classes=[]
		for d in dots:
			nearest = float('inf')
			nearest_dot = None
			for dc in self.DC:
				dist = self.euclidian_dist(d,dc)
				if dist < nearest:
					nearest = dist
					nearest_dot = dc
			if nearest_dot == None:
				print 'Error here!'
			classes.append(nearest_dot.clas)
		#Uncomment bellow to actually change the dots
		#map(lambda a,b: a.clas = b, dots, classes)
		return classes
				

