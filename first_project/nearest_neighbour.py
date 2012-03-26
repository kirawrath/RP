from main import CLASSES_SIZE
def nearest_neighbour(dots):
	m=[]
	for dot in dots:
		m.append(dot.pos)
	distances = []
	for i in m:
		dist = []
		for j in m:
			if i == j:
				continue
			# Euclidian distance
			d = pow(sum(map(lambda a, b: pow(b-a, 2), i, j)), 0.5)
			d = round(d, 3)

			dist.append(d)
			
		distances.append(dist)
	return distances

def k_nearest_neighbour(dots, k):
	m=[]
	for dot in dots:
		m.append(dot.pos)
	distances = nearest_neighbour(dots)
	for idx, line in enumerate(distances):
		#s = sorted(line)
		smallers = []
		votes = []
		for dummy in range(CLASSES_SIZE):
			smallers.append(float('inf'))
		for dummy in line:
			votes.append((0,0)) #(class, dist)

		for i, dist in enumerate(line):
			if dist < smallers[-1]:
				''' index is the dots index.
					As the distances lines has
					(len(dots)-1) entries, this
					index mapping is necessary.
				'''
				index = 0
				if i < idx:
					index = i
				else:
					index = i + 1

				for v_i, v in enumerate(votes):
					if v[1] == 0:
						votes[v_i] = (dots[index].clas, dist)
						#print 'v: ', v
						#print votes
						break
				else:
					for v_i, v in enumerate(votes):
						if v[1] == smallers[-1]:
							votes[v_i] = (dots[index].clas, dist)
					else:
						raise 'Oh noes!'

				smallers[-1] = dist
				smallers.sort()
		results = [0]*CLASSES_SIZE
		for v in votes:
			results[v[0]] += 1
		# The index of the bigger is the chosen one
		bigger=0
		#print 'votes: ', votes
		#print 'results: ', results
		for index, r in enumerate(results):
			if r > bigger:
				bigger = r
				dots[idx].clas = index


	return distances
