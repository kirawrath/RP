from erode import erode

def dilate(imgname, outfile=None):
	return erode(imgname, True, outfile)
