#!/usr/bin/env python
# A simple feedforward neural network that learns XOR.

from xor import SequentialXORDataSet #@UnresolvedImport
from xor import XORDataSet #@UnresolvedImport
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer


def testTraining():
    #d = SequentialXORDataSet()
    d = XORDataSet()
    n = buildNetwork(d.indim, 4, d.outdim, recurrent=True)
    t = BackpropTrainer(n, learningrate = 0.01, momentum = 0.99, verbose = False)
    print 'Training...'
    t.trainOnDataset(d, 1000)
    print 'Testing...'
    t.testOnData(verbose= True)


if __name__ == '__main__':
    testTraining()
