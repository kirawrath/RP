from circle import *
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
						if debug:
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
