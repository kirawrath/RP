#!/usr/bin/env python
import sys
import random
CLASSES_SIZE = 2

class Dot:
	def __init__(self, position):
		self.pos = position
		self.clas = 0 # Point class =)
	def __str__(self):
		return str(self.clas)
	

def hamming(dots):
	m=[]
	for dot in dots:
		m.append(dot.pos)
	distances = []
	for i in m:
		dist=[]
		for j in m:
			# do not calculate itself
			if i == j:
				continue
			hamm = sum(map(lambda a,b: abs(abs(a)-abs(b)), i, j))
			# just to look pretty
			hamm = round(hamm, 3)
			dist.append(hamm)
		distances.append(dist)
	return distances

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

				for v in votes:
					if v[1] == 0:
						v = (dots[index].clas, dist)
						break
				else:
					for v in votes:
						if v[1] == smallers[-1]:
							v = (dots[index].clas, dist)
					else:
						raise 'Oh noes!'
				
				smallers[-1] = dist
				smallers.sort()
		results = [0]*CLASSES_SIZE
		for v in votes:
			results[v[0]] += 1
		# The index of the bigger is the chosen one
		bigger=0
		for index, r in enumerate(results):
			if r > bigger:
				bigger = r
				dots[idx].clas = index


	return distances

def main():
	if len(sys.argv) > 1:
		f = open(sys.argv, 'r')
	else:
		f = open('4Ndatabase_small', 'r')

	dots=[]
	line = f.readline()
	while line != '':
		# Converting the input line into a list of numbers
		values = []
		num = ''
		for i in line:
			if i == ',' or i == '\n':
				values.append(float(num))
				num = ''
				continue
			num += i

		dots.append(Dot(values))
		line = f.readline()

	for dot in dots:
		if random.random()>0.5:
			dot.clas = 0
		else:
			dot.clas = 1
	
	for dot in dots:
		print dot,
	print
	m = k_nearest_neighbour(dots, 2)
	for dot in dots:
		print dot,


if __name__ == '__main__':
	main()
