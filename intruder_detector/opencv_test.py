import cv2
import sys

image=sys.argv[1]
im = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#thresh = cv2.adaptiveThreshold(imgray,255,0,1,11,2)
thresh = im
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	bounding_box=cv2.boundingRect(cnt)
	print bounding_box
