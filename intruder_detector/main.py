from subtract import subtract
from threshold import threshold
from erode import erode
from sys import argv

def main():
	imgname1='imgs/porta1pb.pnm'
	imgname2='imgs/porta2pb.pnm'
	if len(argv)>2:
		imgname1=argv[1]
		imgname2=argv[2]

	print 'Subtracting...'
	subtract(imgname1, imgname2)
	print 'Thresholding...'
	threshold('subtracted_image.png', 75)
	print 'Eroding...'
	erode('thresholded_image.png')

	

if __name__ == '__main__':
	main()
