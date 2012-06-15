from PIL import Image
def threshold(imgname, th = 100):
	img = Image.open(imgname)

	if img.mode != 'L':
		img = img.convert('L')
	
	w, h = img.size
	result = Image.new('1', (w,h))
	
	for i in range(w):
		for j in range(h):
			p = img.getpixel((i,j))
			if p > th:
				p = 1
			else:
				p = 0
			result.putpixel((i,j), p)

	result.save('thresholded_image.png')
	return result
