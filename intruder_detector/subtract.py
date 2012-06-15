from PIL import Image

def subtract(imgname1, imgname2):
	img1 = Image.open(imgname1)
	img2 = Image.open(imgname2)

	assert img1.size == img2.size

	if img1.mode != 'L':
		img1 = img1.convert('L')
	if img2.mode != 'L':
		img2 = img2.convert('L')
	
	w, h = img1.size
	result = Image.new('L', (w,h))
	
	for i in range(w):
		for j in range(h):
			p1 = img1.getpixel((i,j))
			p2 = img2.getpixel((i,j))
			r = abs(p1-p2)
			result.putpixel((i,j), r)
	result.save('subtracted_image.png')
	return result

