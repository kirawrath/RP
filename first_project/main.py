#!/usr/bin/env python
import sys
import random
from pattern_machine import *
from voronoi import *
from interface import *
debug=1
class Dot:
	def __init__(self, position):
		self.pos = position
		self.clas = 0 # Point class =)
	def __str__(self):
		st='('
		for n in self.pos:
			st+=str(n)+', '
		return st.rstrip(', ')+')'
		#return str(self.clas)

def parse_file(f):
	line = f.readline()
	dots=[]
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
		dots.append(d)
		line = f.readline()
	return dots


def main():
	if len(sys.argv) > 1:
		train_file = open(sys.argv[1], 'r')
	else:
		train_file = open('train_file', 'r')
	if len(sys.argv) > 2:
		test_file = open(sys.argv[2], 'r')
	else:
		test_file = open('database', 'r')

	train_dots = parse_file(train_file)
	dots = parse_file(test_file)

	print '''
	Type a number to choose an algorithm.

	1 Nearest Neighbour
	2 K Nearest Neighbour
	3 Hamming Distance
	4 Voronoi
	'''
	inp = raw_input()
	inp = int(inp.rstrip('\n'))
	
	pm = pattern_machine()
	pm.train(train_dots)

	if inp==1:
		pm.nearest_neighbour(dots)
	elif inp==2:
		k=int(raw_input('Type the number k: '))
		pm.k_nearest_neighbour(dots, k)
	elif inp==3:
		pm.hamming(dots)

	if inp!=4:
		print 'Printing the classes chosen:'
		for d in dots:
			print d.clas,
		print
	else:
		vor = Voronoi()
		polys = vor.find_polygons(dots)

		ui = Interface()
		for p in polys:
			ui.add_polygon(p)
			if debug:
				print 'Poly: ',p
		ui.show()
	
	

if __name__ == '__main__':
	main()
