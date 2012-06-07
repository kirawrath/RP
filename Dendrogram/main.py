#!/usr/bin/env python
from matplotlib.pyplot import show
from hcluster import dendrogram
import sys
debug=0
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
		d=values
		dots.append(d)
		line = f.readline()
	return dots
def standartizate(data):
	w=len(data[0])
	h=len(data)
	for j in range(w):
		mean=0
		for i in range(h):
			mean+=data[i][j]
		mean /= h
		stddev = 0
		for i in range(h):
			stddev += pow(data[i][j] - mean, 2)
		stddev = pow(stddev/h, 0.5)
		for i in range(h):
			data[i][j] = (data[i][j] - mean)/stddev			

def eucli_dist(a,b):
	assert len(a) == len(b)
	s=sum(map(lambda x,y: pow(x-y,2),a,b))
	return pow(s,0.5)

def merge(dists, x, y):
	''' Change this function to cicle between
		simple, complete and mean modes '''
	for i, d in enumerate(dists):
		del(dists[i][y])

	for i, d in enumerate(dists[x]):
		dists[x][i] = min(dists[x][i], dists[y][i])

	del(dists[y])
	#Symetrize
	assert x < y
	for i, d in enumerate(dists):
		dists[i][x] = dists[x][i]

def dprint(dist):
	if debug:
		for i in dist:
			for j in i:
				print round(j,2),
			print ''

def agglomerate(dists):
	min_dist = float('inf')
	elected=(-1,-1) #chosen class to merge
	for i, dummy in enumerate(dists):
		for j, d in enumerate(dummy):
			if j >= i:
				break
			if d < min_dist:
				min_dist = d
				elected = (i,j)

	if elected[0] > elected[1]:
		elected = (elected[1],elected[0])
	merge(dists, elected[0], elected[1])

	dprint(dists)

	return dists, elected[0], elected[1], min_dist

def dist_from_data(data):
	dists=[]

	for d in data:
		mydists=[]
		for e in data:
			mydists.append(eucli_dist(e,d))
		dists.append(mydists)
	return dists


def main():
	filename='iris2d.data'
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		print 'Assuming filename \'iris2d.data\''
	data = parse_file(filename)

	minclass = int(raw_input('Minclass: '))
	maxclass = int(raw_input('Maxclass: '))

	standartizate(data)
	dists = dist_from_data(data)
	nick = len(dists)
	lend=nick
	n1 = lend-1
	linkage=[]
	merge_points=[]
	# charlie[index used in dist matrix] = [ new cluster nick, number of children ]
	charlie=dict()
	for i in range(lend):
		charlie[i] = [i,1]
	while n1:
		n1-=1
		dists, e0, e1, d = agglomerate(dists)
		
		#charlie[e0][1] has all the children of both e0 and e1
		charlie[e0][1] = charlie[e0][1] + charlie[e1][1]

		linkage.append([charlie[e0][0], charlie[e1][0], d, charlie[e0][1]])

		#Fixing the indexes due to the deletion of e1
		for i in range(e1,lend-1):
			charlie[i] = charlie[i+1]

		charlie[e0][0] = nick
		nick+=1
		#n1 contains the number of classes
		if n1 <= maxclass and n1 >= minclass:
			merge_points.append(d)
			
	# Finding the cutting point
	max_dist=0
	index=-1
	print merge_points
	for i in range(len(merge_points)-1):
		d = merge_points[i+1] - merge_points[i]
		if d > max_dist:
			max_dist = d
			index = i

	assert index >= 0
	print 'Cutting point is at y='+str(merge_points[index])
	
	print 'Showing the image...'
	
	dendrogram(linkage)
	show()
		


if __name__ == '__main__':
	main()
