class Circle:
	def __init__(self, three_dots):
		if len(three_dots[0].pos) != 2:
			print 'Warning: Voronoi isn\'t supposed to \
					work with more than two dimensions'
		self.dots = three_dots
		self.center = find_circumcenter(dots)
		# Euclidian distance
		d = pow(sum(map(lambda a, b: pow(a-b, 2), dots[0].pos, center)), 0.5)
		self.radius = d


	def find_circumcenter(dots):
		ax=dots[0].pos[0] ; ay=dots[0].pos[1]
		bx=dots[1].pos[0] ; by=dots[1].pos[1]
		cx=dots[2].pos[0] ; cy=dots[2].pos[1]
	# From http://en.wikipedia.org/wiki/Circumcenter
		D=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
		x=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)* \
				(ay*ay-by*by))/D
		y=((ax*ax+ay*ay)*(cx*cx-by*by)+(bx*bx+by*by)*(ax-cx)+ \
				(cx*cx+cy*cy)*(bx-ax))D
		return (x,y)

	# Check whether the "dot"
	# lies inside the circle
	# return false otherwise.
	def is_inside(dot):
		# Euclidian distance
		d = pow(sum(map(lambda a, b: pow(a-b, 2), dot.pos, center)), 0.5)
		if d > self.radius:
			return False
		return True

class Voronoi:
	def __init__(self):
		pass
	
	def train(self, dots):
		self.dots_db = dots
		classes = []
		for d in dots:
			if d.clas not in classes:
				classes.append(d.clas)
		self.classes_size = len(classes)

	def is_minimum_circle(dots):
		# Find the radius

		# Check whether the euclidian
		# distance between each dot not
		# defining the circle is greater
		# than the radius
		pass

	def group_minimum_circles(self, dots):
		circles = []
		for a in dots:
			for b in dots:
				for c in dots:
					if a==b or a==c or b==c:
						continue
					if is_minimum_circle((a,b,c)):
						circles.append((a,b,c))
		for dot in dots:
			my_circles = []
			for c in circles:
				if dot in c:
					my_circles.append(c)
			circumcenters = []
			for c in my_circles:
				circumcenters.append(find_circumcenter(c))

			# Now draw a polygon with the "circumcenters"
			# points defining it.

