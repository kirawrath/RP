from PIL import Image
import sys
from main import Dot
from random import random
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
		colors={}
		for d in dots:
			if d.clas not in colors:
				colors[d.clas] = (int(255*random()),int(255*random()),\
						int(255*random()),255)							
			try:
				self.img.putpixel((int(d.pos[0]),int(d.pos[1])),\
						colors[d.clas])
			except IndexError:
				print int(d.pos[0]), int(d.pos[1])


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
