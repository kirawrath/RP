#!/usr/bin/env python
import sys
import random
from pattern_machine import *

class Dot:
	def __init__(self, position):
		self.pos = position
		self.clas = 0 # Point class =)
	def __str__(self):
		return str(self.clas)


def main():
	if len(sys.argv) > 1:
		train_file = open(sys.argv[1], 'r')
	else:
		train_file = open('2N_train', 'r')
	if len(sys.argv) > 2:
		test_file = open(sys.argv[2], 'r')
	else:
		test_file = open('2Ndatabase_small', 'r')

	train_dots=[]
	line = train_file.readline()
	while line != '':
		# Converting the input line into a list of numbers
		values = []
		num = ''
		line = line.rstrip('\n')
		line = line.replace(',', ' ')
		line = line.split()
		for d in line:
			if d == line[-1]:
				break
			values.append(float(d))
		
		d=Dot(values)
		d.clas = line[-1]
		train_dots.append(d)
		line = train_file.readline()


	dots=[]
	line = test_file.readline()
	while line != '':
		# Converting the input line into a list of numbers
		values = []
		num = ''
		line = line.rstrip('\n')
		line = line.replace(',', ' ')
		line = line.split()
		for d in line:
			values.append(float(d))
		
		d=Dot(values)
		dots.append(d)
		line = test_file.readline()

	#random.shuffle(dots)

	pm = pattern_machine()
	pm.train(train_dots)
	#pm.nearest_neighbour(dots)
	pm.k_nearest_neighbour(dots, 2)

	for d in dots:
		print d,
	print
	


if __name__ == '__main__':
	main()
