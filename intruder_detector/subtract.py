
from PIL import Image

def subtract(imgname1, imgname2):
	img1 = Image.open(imgname1)
	img2 = Image.open(imgname2)

	img1.convert('L')
	img2.convert('L')

	assert img1.size == img2.size
	assert img1.mode == 'L'
	assert img2.mode == 'L'
	
	w, h = img1.size
	result = Image.new('L', (w,h))
	
	
	for i in range(w):
		for j in range(h):
			p1 = img1.getpixel((i,j))
			p2 = img2.getpixel((i,j))
			r = map(lambda a,b: abs(a-b), p1, p2)
			r = sum(r)/len(r)
			result.putpixel((i,j), r)
	result.save('subtracted_image.jpg')


def test():
	subtract('99.png', '100.png')

if __name__ == '__main__':
	test()
