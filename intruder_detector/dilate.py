from erode import erode

kernel = [[1, 1, 1],
		  [1, 1, 1],
		  [1, 1, 1]]

def dilate(imgname):
	return erode(imgname, True)
