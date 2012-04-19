#--*--coding: utf8 --*--
import random
from dot import Dot
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
		nearest_dot = Dot((),()) #Just a fake dot
		for d in dots:
			nearest = float('inf')
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
	def acceptable(self, dotinfo, nclasses, ntotal, z):
		clas = str(dotinfo['dot'].clas)
		p = float(dotinfo['hits']) / nclasses[clas]
		n = dotinfo['num_tries']

		first = p+z*z/(2*n)
		second = z*pow( p*(1-p)/n + (z*z)/(4*n*n) ,0.5)
		dem = 1+(z*z)/n

		iplower = (first - second)/dem
		ipupper = (first + second)/dem


		p = float(nclasses[clas])/sum([nclasses[i] for i in iter(nclasses)])
		n = ntotal

		first = p+z*z/(2*n)
		second = z*pow( p*(1-p)/n + (z*z)/(4*n*n) ,0.5)
		dem = 1+(z*z)/n

		iflower = (first - second)/dem
		ifupper = (first + second)/dem

		if z < 0.8 and ipupper < iflower:
			return 'discard'
		if ifupper < iplower:
			return True
		return False

	def train(self,dots):
		criteria = [] #Data Structure to manage DC.
		nclasses = {}
		newd = {}
		newd['dot'] = dots[0] ; newd['dist'] = 0
		newd['hits'] = 0 ; newd['num_tries'] = 1
		criteria.append(newd)
		nclasses[str(dots[0].clas)] = 1
		#criteria = {dot,dist,hits,num_tries,}
		# Usage:
		# criteria[3]['dot'] <- to get the dot indexed by 3
		hit=0; miss=0
		accep = 0.9
		discard = 0.75
		dots_processed=0
		for d in dots[1:]:
			dots_processed+=1
			clas = str(d.clas)
			if clas in nclasses:
				nclasses[clas] += 1
			else:
				nclasses[clas] = 1

			for dc in criteria:
				dist = self.euclidian_dist(d,dc['dot'])
				dc['dist'] = dist
				
			#2.2
			criteria.sort(key = lambda a: a['dist'])
			nearest = None # just initializing with anything
			for dc in criteria:
				if self.acceptable(dc, nclasses, dots_processed, accep):
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
				# Update IP
			else:
				miss += 1
				newd = {}
				newd['dot'] = d ; newd['dist'] = 0
				newd['hits'] = 0 ; newd['num_tries'] = 0
				criteria.append(newd)

			#2.4
			deads=[] #dots marked for removal
			for dc in criteria:
				if dc['dist'] <= nearest['dist']:
					dc['num_tries'] += 1
					# se registro se classificação for ruim:
					if self.acceptable(dc, nclasses, dots_processed, discard) == 'discard':
						#WARNING: NEVER REMOVE DURING AN ITERATION!!!
						if dc['num_tries'] > 30:
							deads.append(dc)
			for dead in deads:
				del( criteria[criteria.index(dead)] )

		self.DC = [i['dot'] for i in criteria]
		print 'DC length: ',len(self.DC)
		return (self.DC, hit, miss)



