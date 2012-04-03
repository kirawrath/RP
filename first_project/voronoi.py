class Circle:
	def __init__(self, three_dots):
		if len(three_dots[0].pos) != 2:
			print 'Warning: Voronoi isn\'t supposed to \
					work with more than two dimensions'
		self.dots = three_dots
		self.center = self.find_circumcenter(self.dots)
		#check if those points are collinear
		if self.center == None:
			#print 'Collinear points, couldn\'t make a circle from that.'
			return None
		# Euclidian distance
		d = pow(sum(map(lambda a, b: pow(a-b, 2), self.dots[0].pos, self.center)), 0.5)
		self.radius = d
		
	def __str__(self):
		st=''
		for d in self.dots:
			st+=' '+str(d)
		return 'r: '+str(round(self.radius,1))+' c: '+str(self.center)+' dots:'+st

	def __contains__(self, item):
		return (item in self.dots)
	
	def __cmp__(self,other):
		if self.center==other.center \
				and self.radius==other.radius:
			return 0
		return 1

	def find_circumcenter(self, dots):
		ax=dots[0].pos[0] ; ay=dots[0].pos[1]
		bx=dots[1].pos[0] ; by=dots[1].pos[1]
		cx=dots[2].pos[0] ; cy=dots[2].pos[1]

		D=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
		if D == 0: # Collinear
			return None
	# From http://en.wikipedia.org/wiki/Circumcenter
		x=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)* \
				(ay*ay-by*by))/D
		y=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+ \
				(cx*cx+cy*cy)*(bx-ax))/D
		return (x,y)

	# Check whether the "dot"
	# lies inside the circle
	# return false otherwise.
	def is_inside(self, dot):
		# Euclidian distance
		d = pow(sum(map(lambda a, b: pow(a-b, 2), dot.pos, self.center)), 0.5)
		if d > self.radius:
			return False
		return True
	def is_minimum(self, dots):
		if self.center == None:
			return False

		for d in dots:
			if d not in self.dots:
				dist = pow(sum(map(lambda a, b: pow(a-b, 2), d.pos, self.center)), 0.5)
				if dist <= self.radius:
					return False
		#print 'min:', self.radius, self.center
		return True



class Voronoi:
	def __init__(self):
		pass

	def find_polygons(self, dots):
		circles = []
		polygons = []
		ldots=len(dots)
		for i in range(ldots):
			for j in range(i+1,ldots):
				for k in range(j+1,ldots):

					circle = Circle([dots[i],dots[j],dots[k]])
					#checking if collinear
					if circle.center is None:
						continue

					if circle.is_minimum(dots):
						print circle
						circles.append(circle)
		
		# Now I have all the minimum circles!
		
		# Find all triangles that a given dot
		# is a vertex.
		for dot in dots:
			circumcenters = []
			for c in circles:
				if dot in c:
					circumcenters.append(c.center)

			polygons.append(circumcenters)
		# Now draw a polygon with the "circumcenters"
		# points defining it.
		return polygons
