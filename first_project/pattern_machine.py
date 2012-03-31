class pattern_machine:
	def __init__(self):
		self.dots_db = []
		
	def train(self, dots):
		self.dots_db = dots
		classes = []
		for d in dots:
			if d.clas not in classes:
				classes.append(d.clas)
		self.classes_size = len(classes)

	def nearest_neighbour(self, dots):
		for dot in dots:
			dist = float('inf')
			for dbdot in self.dots_db:
				# Euclidian distance
				d = pow(sum(map(lambda a, b: pow(b-a, 2), dot.pos, dbdot.pos)), 0.5)
				d = round(d, 3)
				if d < dist:
					dist = d
					dot.clas = dbdot.clas

				
	def k_nearest_neighbour(self, dots, k):
		if k%2==0 or k>=self.classes_size:
			print 'Warning: Bad choice of k'

		for dot in dots:
			voters = [(0,float('inf'))]*k
			for dbdot in self.dots_db:
				# Euclidian distance
				d = pow(sum(map(lambda a, b: pow(b-a, 2), dot.pos, dbdot.pos)), 0.5)
				d = round(d, 3)

				if d < voters[-1][1]:
					voters[-1] = (dbdot, d)
					voters.sort(key=lambda a: a[1])

			# Counting number of votes
			votes = []
			for v in voters:
				if v[0].clas not in votes:
					votes.append((v[0].clas, 1)) #(candidate, num of votes)
				else:
					for x in votes:
						if x[0] == v[0].clas:
							 x[1] += 1
							 break
					else:
						raise 'Oh Noes!'
			# Finding the most voted one
			bigger = 0
			bigger_index=0
			for i, v in enumerate(votes):
				if v[1] > bigger:
					bigger = v[1]
					bigger_index = i

			dot.clas = votes[bigger_index][0]
			#print 'votes', votes


	def hamming(dots):
		for dot in dots:
			dist = float('inf')
			for dbdot in self.dots_db:
				d = sum(map(lambda a,b: abs(abs(a)-abs(b)), i, j))
				d = round(d, 3)
				if d < dist:
					dist = d
					dot.clas = dbdot.clas
