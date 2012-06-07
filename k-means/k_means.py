from utilities import *
def k_means(k, dots):
	standartizate(dots)
	centroids=init_centroids(dots, k)

	moved = True
	while moved:
		moved = False
		# Assign Step
		for i, d in enumerate(dots):
			nearest_i = float('inf')
			nearest_d = float('inf')
			for j, c in enumerate(centroids):
				dist = eucli_dist(d.pos, c.pos)
				if dist < nearest_d:
					nearest_d = dist
					nearest_i = j
			if d.clas != nearest_i:
				moved = True
				dots[i].clas = nearest_i

		# Update Centroids Step
		means = [ [0]*len(dots[0].pos) for _ in range(k)]
		sizes = [0]*k

		for d in dots:
			clas = d.clas
			sizes[clas] += 1
			means[clas]=map(lambda a,b: a+b, means[clas], d.pos)
		for i, m in enumerate(means):
			assert len(means) == len(sizes)
			x = map(lambda a: float(a)/sizes[i], m)
			centroids[i] = Dot(x, i)

	mean_total = [0]*len(dots[0].pos)
	for c in centroids:
		mean_total = map(lambda a,b: a+b, mean_total, c.pos)
	mean_total = map(lambda a: float(a)/len(dots), mean_total)
	gsizes = [0]*k
	for d in dots:
		gsizes[d.clas] += 1
	sq_entre = 0
	for i in range(k):
		x = map(lambda a,b: a-b, centroids[i].pos, mean_total)
		#x^2
		x = sum(map(lambda a: a*a, x))
		sq_entre += gsizes[i] * x
	sq_total = 0
	for i in range(k):
		for j in range(gsizes[i]):
			x = map(lambda a,b: a-b, i_element(dots, i, j), mean_total)
			x = sum(map(lambda a: a*a, x))
			sq_total += x
	sq_dentro = sq_total - sq_entre
	d1 = k-1
	d2 = len(dots) - k
	mean_sq_entre = sq_entre/d1
	mean_sq_dentro = sq_dentro/d2
	
	f0 = mean_sq_entre/mean_sq_dentro
	f = read_table(d1,d2)

	return f0,f,d1,d2
