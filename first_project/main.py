#!/usr/bin/env python
import sys

def hamming(m):
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

def nearest_neighbour(m):
	distances = []
	for i in m:
		dist = []
		for j in m:
			if i == j:
				continue
			# Euclidian distance
			d = pow(sum(map(lambda a, b: pow(b-a, 2), i, j)), 0.5)

			dist.append(d)
			
		distances.append(dist)
	return distances


def main():
	f = open('4Ndatabase', 'r')

	matrix=[]
	line = f.readline()
	while line != '':
		# Converting the line into a list of numbers
		values = []
		num = ''
		for i in line:
			if i == ',' or i == '\n':
				values.append(float(num))
				num = ''
				continue
			num += i

		matrix.append(values)
		line = f.readline()
	
	#print hamming(matrix)
	print nearest_neighbour(matrix)


if __name__ == '__main__':
	main()