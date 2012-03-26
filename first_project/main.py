#!/usr/bin/env python
import sys
import random
CLASSES_SIZE = 2
from nearest_neighbour import *

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
			dot.clas = 1
		else:
			dot.clas = 0
	
	for dot in dots:
		print dot,
	print
	m = k_nearest_neighbour(dots, 2)
	for dot in dots:
		print dot,


if __name__ == '__main__':
	main()
