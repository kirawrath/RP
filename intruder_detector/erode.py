from PIL import Image
kernel = [[1, 1, 1],
		  [1, 1, 1],
		  [1, 1, 1]]

def erode(imgname):
	img = Image.open(imgname)

	if img.mode != '1':
		img = img.convert('1')
	
	w, h = img.size
	result = Image.new('1', (w,h))
	lk = int(len(kernel)/2)
	
	for i in range(1, w-1):
		for j in range(1, h-1):
			r = 0
			for x in range (-lk, lk + 1):
				for y in range(-lk, lk + 1):
					p = img.getpixel((i+x,j+y))
					if p*kernel[x+1][y+1] == 0:

						todo!
						
						r=1
						break
				if r:
					break
			result.putpixel((i,j), r)

	result.save('eroded_image.png')
	return result
