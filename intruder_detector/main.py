from subtract import subtract
from threshold import threshold
from erode import erode
from dilate import dilate
from sys import argv
import cv2

def main():
	imgname1='imgs/porta1pb.pnm'
	imgname2='imgs/larapiopb.pnm'
	if len(argv)>2:
		imgname1=argv[1]
		imgname2=argv[2]

	thresh_factor = 65
	min_size = 10 #(minimum w and h to be not considered noise)



	print 'Subtracting...'
	subtract(imgname1, imgname2)
	print 'Thresholding...'
	threshold('subtracted_image.png', 65)
	print 'Eroding...'
	k=open('kernel', 'w')
	k.write('''1 1 1 1 1
	1 1 1 1 1
	1 1 1 1 1''')
	k.close()
	erode('thresholded_image.png')
	print 'Dilating...'
	dilate('eroded_image.png')

	#Dilating to merge pieces, then erode to get back to the original size

	print 'Merging pieces...',
	k=open('kernel', 'w')
	for i in range(10):
		k.write('1 1 1 1 1 1 1 1 1 1\n')
	k.close()
	dilate('dilated_image.png', outfile='result0.png')
	print 'halfway done...'
	erode('result0.png', outfile = 'result.png')

	#Using opencv to calculate the bounding box to figure out what we found

	img = cv2.imread('result.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
	contours, hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

	noise=0
	for cnt in contours:
		b_box = cv2.boundingRect(cnt)
		w,h = b_box[2], b_box[3]
		#print w,h
		if w > min_size and h > min_size:
			#Found something...
			if w > h:
				print 'Found a dog!'
			else:
				print 'Found an intruder!'
		else:
			noise+=1
	print 'Found',str(noise),'noise(s).'
	

if __name__ == '__main__':
	main()
