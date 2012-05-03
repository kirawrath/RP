#!/usr/bin/env python
from backprop import backproptrainer
from digits_dataset import DigitsDataSet
from pybrain.tools.shortcuts import buildNetwork
import sys
import os
def testTraining():

	output=''
	img_names = []
	assert len(sys.argv)>1

	if sys.argv[1] == '--no-cv':
		img_names = os.listdir('./dataset')
		img_names = map(lambda a: './dataset/'+a, img_names)
		output = 'output'
	else:
		assert len(sys.argv)==(1+10+1), 'Numero errado de argumentos'
		img_names = sys.argv[1:11]
		output = sys.argv[11]

	hidden_layers = 2
	epochs = 10000

	d = DigitsDataSet(img_names)
	n = buildNetwork(d.indim, hidden_layers, d.outdim, recurrent=True)
	t = backproptrainer(n, dataset = d, learningrate = 0.01, momentum = 0.1, verbose = False)

	print 'Training...'
	for _ in range(epochs):
		t.train()

	print 'Testing...'
	_, results = t.testOnData(verbose= True)
	

	f = open(output, 'w')
	print 'Writing to file \"'+output+'\"'
	for r in results:
		st='output:\t'+str(r[0])+'\n'
		st+='real value:\t'+str(r[1])+'\n'
		st+='error:\t'+str(r[2])+'\n'
		st+='-'*15 + '\n'
		f.write(st)


if __name__ == '__main__':
	testTraining()
