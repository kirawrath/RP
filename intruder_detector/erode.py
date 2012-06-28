from PIL import Image
'''
kernel = [[0, 1, 0],
		  [1, 1, 1],
		  [0, 1, 0]]
'''
def erode(imgname, dilate=False, outfile=None):
	kf = open('kernel')
	st = kf.readline()
	kernel=[]
	while st!='':
		st=map(lambda a:int(a), st.split())
		kernel.append(st)
		st=kf.readline()

	img = Image.open(imgname)
	aux = 0
	if dilate:
		aux = 255

	if img.mode != '1':
		print 'Wrong image format, converting to bicolor...'
		img = img.convert('1')
	
	w, h = img.size
	result=None
	if dilate:
		result = Image.new('1', (w,h), 255)
	else:
		result = Image.new('1', (w,h)) #black image
	lk = int(len(kernel)/2)
	
	for i in range(w):
		for j in range(h):
			if img.getpixel((i,j)) != aux:
				e=int(not aux)*255
				for x in range (-lk, lk + 1):
					for y in range(-lk, lk + 1):
						if kernel[x+1][y+1] == 1:
							if i+x<0 or j+y<0 or j+y >= h or i+x >= w:
								p=0
							else:
								p = img.getpixel((i+x,j+y))
							if p == aux:
								e = aux
								break
					if e==aux:
						break
				result.putpixel((i,j), e)

	if dilate:
		if outfile == None:
			outfile = 'dilated_image.png'
		result.save(outfile)
	else:
		if outfile == None:
			outfile = 'eroded_image.png'
		result.save(outfile)
	return result
