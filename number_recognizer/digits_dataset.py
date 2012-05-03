#!/usr/bin/env python
from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import fListToString
from PIL import Image
import os
from string import rfind

class DigitsDataSet(SupervisedDataSet):
	def __init__(self, imgnames=None):
		SupervisedDataSet.__init__(self, 10*15, 1)
		'''
		if imgnames==None:
			imgnames = os.listdir('./dataset')
			map(lambda a: './dataset/'+a, imgnames)
		'''
		imgnames.sort()

		for iname in imgnames:
			img = Image.open(iname)
			w,h = img.size
			assert(w*h==150)
			pixels=[]
			for i in range(w):
				for j in range(h):
					p = img.getpixel((i,j))
					#All the 3 fields of p are equal, always.
					#Therefore we need only one to represent.
					pixels.append(float(p[0])/255)

			num = iname[rfind(iname,'/')+1:rfind(iname,'.')]
			assert(len(pixels)==150)
			self.addSample(pixels, [int(num)])

	def _evaluateSequence(self, f, seq, verbose = False):
		"""Return the ponderated MSE over one sequence."""
		totalError = 0.
		ponderation = 0.
		for input, target in seq:
			res = f(input)
			e = 0.5 * sum((target-res).flatten()**2)
			totalError += e
			ponderation += len(target)
			if verbose:
				resultado = (fListToString(list(res)),
						fListToString(target),
						e)
				print 'out:	', resultado[0]
				print 'correct:', resultado[1]
				print 'error: % .8f' % resultado[2]
		return totalError, ponderation, resultado
