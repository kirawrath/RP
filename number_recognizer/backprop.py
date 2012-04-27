#!/usr/bin/env python

from digits import DigitsDataSet #@UnresolvedImport
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer


def testTraining():
	hidden_layers = 2
	d = DigitsDataSet()
	n = buildNetwork(d.indim, hidden_layers, d.outdim, recurrent=True)
	t = BackpropTrainer(n, dataset = d, learningrate = 0.01, momentum = 0.1, verbose = False)

	print 'Training...'
	for _ in range(10000):
		t.train()

	print 'Testing...'
	t.testOnData(verbose= True)


if __name__ == '__main__':
	testTraining()
