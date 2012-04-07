#!/usr/bin/env python
import sys
import random
from interface import *
from ibl import *
debug=1
class Dot:
	def __init__(self, position):
		self.pos = position
		self.clas = 0 # Point class =)
	def __str__(self):
		st='('
		for n in self.pos:
			st+=str(n)+', '
		st = st.rstrip(', ')+')'
		st += ' c: '+str(self.clas)+'.'
		return st

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

	1 IBL 1
	2 IBL 2
	3 IBL 3
	'''
	inp=''
	if not debug:
		inp = raw_input()
		inp = int(inp.rstrip('\n'))
	else:
		inp = '1'
	
	ibl = None
	if inp == '1':
		ibl = IBL1()
	elif inp == '2':
		ibl = IBL2()
	elif inp == '3':
		ibl = IBL3()
	else:
		print 'Invalid Option, aborting...'
		sys.exit(0)

	result = ibl.train(train_dots)
	for d in result[0]:
		print d,
	print '\nHit: '+str(result[1])+\
			'\nMiss: '+str(result[2])
	classes = ibl.classify(dots)
	print classes

	if len(dots[0].pos) == 2:
		pass # Plot the dots

	

if __name__ == '__main__':
	main()
