from PIL import Image
import sys

class Img:
	def __init__(self,imgname=None):
		if imgname != None:
			self.parse_train_image(imgname)

	def get_size(self):
		return self.img.size	

	def set_img(self, img):
		self.img=img
	def show(self):
		self.img.show()

	def copy(self):
		img = Img()
		img.set_img(Image.new('RGBA',self.img.size))
		return img

	def paint(self, dots):
		for d in dots:
			try:
				if d.clas=='g':
					self.img.putpixel((int(d.pos[0]),int(d.pos[1])),\
							(255,255,0,255))
				elif d.clas=='p':
					self.img.putpixel((int(d.pos[0]),int(d.pos[1])),\
							(255,0,0,255))
				else:
					'Whaaat?'
			except IndexError:
				pass


	def parse_train_image(self,imgname):
		self.img = Image.open(imgname)
		l = list(self.img.getdata())
		w,h = self.img.size
		tfile = open('train_file', 'w')
		try:
			for i in range(h):
				for j in range(w):
					p = self.img.getpixel((i,j))
					if sum(p) != 0:
						st=str(i)+','+str(j)
						if p[0] == 0:
							st+=',g'
						else:
							st+=',p'
						tfile.write(st+'\n')
		except IndexError:
			pass
		tfile.close()

	

if __name__ == '__main__':
	output_image(sys.argv[1])
