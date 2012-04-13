
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
	def acceptable(y):
		print 'not implemented yet!'
		return False

	def train(self,dots):
		criteria = [] #Data Structure to manage DC.
		#criteria = {dot,dist,hits,num_tries,IP}
		# Usage:
		# criteria[3]['dot'] <- to get the dot indexed by 3
		hit=0; miss=0
		accep = 5
		for d in dots:
			for dc in criteria:
				dist = self.euclidian_dist(d,dc['dist'])
				dc['dist'] = dist
				
			#2.2
			criteria.sort(lambda a: a['dist'])
			nearest = criteria[0] # just initializing with anything
			for dc in criteria:
				if self.acceptable(dc):
					nearest = dc
					break					
			else:
				r = random.random()
				r = int(r*len(criteria))
				nearest = criteria[r]
			#2.3
			if nearest['dot'].clas == d.clas:
				hit += 1
				# Update that dot register
				nearest['num_tries'] += 1
				nearest['hits'] += 1
				# Update IP?
			else:
				miss += 1
				newd = {}
				newd['dot'] = d ; newd['dist'] = 0
				newd['hits'] = 0 ; newd['num_tries'] = 0
				newd['IP'] = 0 #??
				criteria.append(newd)
			#2.4
			deads=[] #dots marked for removal
			for dc in criteria:
				if dc['dist'] <= nearest['dist']:
					dc['num_tries'] += 1
					#dc['IP'] ??
					# se registro se classificação for ruim:
					if True:
						#WARNING: NEVER REMOVE DURING AN ITERATION!!!
						deads.append(dc)
			for dead in deads:
				del( criteria[criteria.index(dead)] )

		return ([i['dots'] for i in criteria], hit, miss)





