from PIL import Image
kernel = [[1, 1, 1],
		  [1, 1, 1],
		  [1, 1, 1]]

def erode(imgname):
	img = Image.open(imgname)

	if img.mode != '1':
		print 'Wrong image format, converting to bicolor...'
		img = img.convert('1')
	
	w, h = img.size
	result = Image.new('1', (w,h))
	lk = int(len(kernel)/2)
	
	for i in range(1, w-1):
		for j in range(1, h-1):
			if img.getpixel((i,j)) != 0:
				e = 1
				for x in range (-lk, lk + 1):
					for y in range(-lk, lk + 1):
						if kernel[x+1][y+1] == 1:
							p = img.getpixel((i+x,j+y))
							if p == 0:
								e = 0
								break
					if e==0:
						break
				result.putpixel((i,j), e)
	

	result.save('eroded_image.png')
	return result
