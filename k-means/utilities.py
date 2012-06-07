from random import random
from dot import Dot
from IBL.ibl import IBL1
from IBL.img_handler import Img
from PIL import Image
def standartizate(dots):
	w=len(dots[0].pos)
	h=len(dots)
	for j in range(w):
		mean=0
		for i in range(h):
			mean+=dots[i].pos[j]
		mean /= h
		stddev = 0
		for i in range(h):
			stddev += pow(dots[i].pos[j] - mean, 2)
		stddev = pow(stddev/h, 0.5)
		for i in range(h):
			dots[i].pos[j] = (dots[i].pos[j] - mean)/stddev			
def eucli_dist(a,b):
	assert len(a) == len(b)
	s=sum(map(lambda x,y: pow(x-y,2),a,b))
	return pow(s,0.5)


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
			values.append(float(d))
		d=Dot(values)
		dots.append(d)
		line = f.readline()
	return dots

def init_centroids(dots, k):
	# Random classes for everyone!
	for i,d in enumerate(dots):
		r = int(random() * k)
		dots[i].clas = r

	#Calculate centroids
	centroids = [ Dot([0,0]) for _ in range(k)]
	means = [ [0]*len(dots[0].pos) for _ in range(k)]
	sizes = [0]*k

	for d in dots:
		clas = d.clas
		sizes[clas] += 1
		means[clas]=map(lambda a,b: a+b, means[clas], d.pos)
	for i, m in enumerate(means):
		assert len(means) == len(sizes)
		assert len(means) == len(centroids)
		x = map(lambda a: float(a)/sizes[i], m)
		centroids[i] = Dot(x, i)
	return centroids

def i_element(dots, clas, i):
	j=0
	for d in dots:
		if d.clas == clas:
			if i==j:
				return d.pos
			j+=1

def read_table(v1,v2):
	f=None
	if v1 > 10 and v1 <= 20:
		f = open('table2')
		v1 -= 10
	else:
		f = open('table')
		
	if v2 > 100:
		v2 = 100
	assert v1 <= 10
	i=1
	line = f.readline()
	while i < v2:
		line = f.readline()
		i+=1
	line = line.split()
	result = float(line[v1-1])
	f.close()
	return result


def use_ibl(dots):
	if len(dots[0].pos) != 2:
		return

	xmax = max([d.pos[0] for d in dots])
	ymax = max([d.pos[1] for d in dots])
	xmin = min([d.pos[0] for d in dots])
	ymin = min([d.pos[1] for d in dots])
	
	if xmin < 0:
		for i, d in enumerate(dots):
			dots[i].pos[0] = d.pos[0] - xmin
		xmax -= xmin
		xmin = 0
	if ymin < 0:
		for i, d in enumerate(dots):
			dots[i].pos[1] = d.pos[1] - ymin
		ymax -= ymin
		ymin = 0

	ibl = IBL1()
	ibl.train(dots)
	rands = ibl.rand_dots(10000)
	ibl.classify(rands)

	h, w = 300, 300

	for i, r in enumerate(rands):
		t=[0]*2
		t[0] = (r.pos[0]/(xmax-xmin))*w
		t[1] = (r.pos[1]/(ymax-ymin))*h
		assert t[0] < w and t[1] < h
		rands[i].pos = t

	newimg = Img('IBL.png')
	newimg.set_img(Image.new('RGBA',(w,h)))
	newimg.paint(rands)
	print 'Showing an image '+str(w)+'x'+str(h)+' now.'
	newimg.show()
