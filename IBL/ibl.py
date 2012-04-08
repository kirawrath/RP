
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
		for i,d in enumerate(dots):
			dots[i].clas = classes[i]
		return classes

class IBL2(IBL1):

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

class IBL3(IBL1):
	def train(self,dots):
		self.DC=[]
		self.criteria = []
		hit=0; miss=0
		accep = 5
		for d in dots:
			dists = []
			for dc in self.DC:
				dist = self.euclidian_dist(d,dc)
				dists.append((dc, dist))

			#2.2
			dists.sort(lambda a: a[1])
			nearest_dot, nearest_dist = dists[0]

			if nearest_dist < accep: # Acceptable
				pass
			else:
				r = random.random()
				r = int(r*len(dists))
				nearest_dot, nearest_dist = dists[r]
			#2.3
			if nearest_dot.clas == d.clas:
				hit += 1
				# Update that dot register
				if nearest_dot in map(lambda a:a[0], self.criteria):
					for i, carl in enumerate(self.criteria):
						if carl == nearest_dot:
							self.criteria[i][1]+=1
				else:
					self.criteria.append([nearest_dot, 1, 0])
			else:
				miss += 1
				self.DC.append(d)
				dists.append((d,0)) # Not sure
			#2.4
			#TODO

				#(dot, acertos, num_rodadas)
		return (self.DC, hit, miss)





