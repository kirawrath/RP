#!/usr/bin/env python
import sys
import random
from ibl import *
from img_handler import *
from random import random
debug=0
class Dot:
	#def __init__(self, position):
	#	self.pos = position
	#	self.clas = 0 # Point class =)
	def __init__(self, position, clas=None):
		self.pos = position
		if clas != None:
			self.clas = clas

	def __str__(self):
		return str(self.clas)
def main():
	if len(sys.argv)>1:
		img = Img(sys.argv[1])
	else:
		print 'No argument given, defaulting to \'./double.png\''
		img = Img('double.png')
	

	train_dots = img.parse_train_image()
	#dots = parse_file(test_file)

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
		inp = 1
	
	ibl = None
	if inp == 1:
		ibl = IBL1()
	elif inp == 2:
		ibl = IBL2()
	elif inp == 3:
		ibl = IBL3()
	else:
		print 'Invalid Option, aborting...'
		sys.exit(0)

	result = ibl.train(train_dots)
	if debug:
		for d in result[0]:
			print d,
	print '\nHit: '+str(result[1])+\
			'\nMiss: '+str(result[2])
	
	if len(train_dots[0].pos) == 2: #Bidimensional
	# Show result in an image
		newimg = img.new()
		w,h = img.get_size()
		randdots=[]
		numrand = 30000
		for dummy in range(numrand):
			d=Dot((int(w*random()), int(h*random())))
			randdots.append(d)

		print 'Generating image with '+str(numrand)+' random points...'
		ibl.classify(randdots)
		newimg.paint(randdots)
		print 'Showing Image now.'
		newimg.show()

		###Sequential###########################
		inp='Do you want to create an image using all pixels?'
		inp+=' (it takes approximately 1 minute). [y/n] '
		inp = raw_input(inp)
		if inp == 'y':
			print 'Creating a matrix with sequential points...'
			seqdots=[]
			for i in range(0,w):
				for j in range(0,h):
					seqdots.append(Dot((i,j)))
			newimg = img.new()
			print 'Classifying...'
			ibl.classify(seqdots)
			print 'Painting...'
			newimg.paint(seqdots)
			print 'Showing Image now.'
			newimg.show()


if __name__ == '__main__':
	main()
