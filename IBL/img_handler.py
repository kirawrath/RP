from PIL import Image
import sys
from main import Dot
class Img:
	def __init__(self,imgname=None):
		self.imgname = imgname

	def get_size(self):
		return self.img.size	

	def set_img(self, img):
		self.img=img
	def show(self):
		self.img.show()

	def new(self):
		img = Img()
		img.set_img(Image.new('RGBA',self.img.size))
		return img

	def paint(self, dots):
		for d in dots:
			try:
				self.img.putpixel((int(d.pos[0]),int(d.pos[1])),\
						d.clas)
			except IndexError:
				print 'IndexError! (img)'


	def parse_train_image(self):
		self.img = Image.open(self.imgname)
		l = list(self.img.getdata())
		w,h = self.img.size
		dots=[]
		try:
			for i in range(w):
				for j in range(h):
					p = self.img.getpixel((i,j))
					if sum(p) != 0:
						dots.append(Dot((i,j), p))
		except IndexError:
			print 'IndexError! (parsing)'
		return dots
