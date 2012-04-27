#!/usr/bin/env python
from pybrain.datasets import SupervisedDataSet
from PIL import Image
import os
from string import find
debug=1
class XORDataSet(SupervisedDataSet):
	def __init__(self):
		SupervisedDataSet.__init__(self, 10*15, 1)
		
		imgnames = os.listdir('./dataset')
		for iname in imgnames:
			img = Image.open('./dataset/'+iname)
			w,h = img.size
			assert(w*h==150)
			pixels=[]
			for i in range(w):
				for j in range(h):
					p = img.getpixel((i,j))
					#All the 3 fields of p are equal, always.
					#Therefore we need only one to represent.
					pixels.append(float(p[0])/255)

			num = iname[:find(iname,'.')]
			assert(len(pixels)==150)
			self.addSample(pixels, [int(num)])
