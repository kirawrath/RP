#!/usr/bin/env python
import sys
import random
from ibl import *
from img_handler import *
from random import random
from PIL import Image
from dot import Dot
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

def parse_file(filename):
	f = open(filename)
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
	if len(sys.argv)>1:
		img = Img(sys.argv[1])
	else:
		print 'No argument given, defaulting to \'./double.png\''
		try:
			img = Img('double.png')
		except IOError:
			print 'No \'double.png\' image found!'
		
		
	inp='Do you want to load a text file? [y/N] '
	inp = raw_input(inp)
	withfile=False
	if inp == 'y':
		inp='Filename (default: \'test.data\'): '
		inp = raw_input(inp)
		if inp == '':
			print 'Defaulting to \'test.data\''
			inp = 'test.data'
		train_dots = parse_file(inp)
		withfile = True
	else:
		train_dots = img.parse_train_image()

	print '''
	Type a number to choose an algorithm.

	1 IBL 1
	2 IBL 2
	3 IBL 3
	'''
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
	
	if withfile:
		xmax = max([d.pos[0] for d in train_dots])
		ymax = max([d.pos[1] for d in train_dots])
		w, h = int(xmax*1.4),int(ymax*1.4) #Create an image 40% larger than the
											# dots range
	else:
		w,h = img.get_size()

	numrand = 30000
	print 'Generating '+str(numrand)+' random points...'
	randdots = ibl.rand_dots(numrand)

	print 'Classifying'+'.'*3
	ibl.classify(randdots)

	print 'Printing output to file \'output\' in the current folder.'
	print 'Outputing the classification of 3000 points.'
	out = open('output', 'w')
	for d in train_dots:
		st=''
		for p in d.pos:
			st += str(p)+','
		st += str(d.clas)+'\n'
		out.write(st)


	if len(train_dots[0].pos) == 2: #Bidimensional
	# Show result into an image
		
		newimg = Img('IBL.png')
		newimg.set_img(Image.new('RGBA',(w,h)))
		newimg.paint(randdots)
		print 'Showing an image '+str(w)+'x'+str(h)+' now.'
		newimg.show()

		###Sequential###########################
		inp='Do you want to create an image using all pixels?'
		inp+=' (it takes approximately 1 minute). [y/N] '
		inp = raw_input(inp)
		if inp == 'y':
			print 'Creating a matrix with sequential points...'
			seqdots=[]
			for i in range(0,w):
				for j in range(0,h):
					seqdots.append(Dot((i,j)))
			newimg = Img('IBL.png')
			newimg.set_img(Image.new('RGBA',(w,h)))
			print 'Classifying...'
			ibl.classify(seqdots)
			print 'Painting...'
			newimg.paint(seqdots)
			print 'Showing Image now.'
			newimg.show()


if __name__ == '__main__':
	main()
