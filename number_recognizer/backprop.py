from pybrain.supervised import BackpropTrainer

class backproptrainer(BackpropTrainer):
	def __init__(self, module, dataset=None, learningrate=0.01, lrdecay=1.0,
				momentum=0., verbose=False, batchlearning=False,
				weightdecay=0.):
		BackpropTrainer.__init__(self, module, dataset, learningrate, lrdecay,
				momentum, verbose, batchlearning, weightdecay)
	
	def testOnData(self, dataset=None, verbose=False):
		"""Compute the MSE of the module performance on the given dataset.

		If no dataset is supplied, the one passed upon Trainer initialization is
		used."""
		if dataset == None:
			dataset = self.ds
		dataset.reset()
		if verbose:
			print '\nTesting on data:'
		errors = []
		importances = []
		ponderatedErrors = []
		results=[]
		for seq in dataset._provideSequences():
			self.module.reset()
			e, i, result = dataset._evaluateSequence(self.module.activate, seq, verbose)
			results.append(result)
			importances.append(i)
			errors.append(e)
			ponderatedErrors.append(e / i)
		if verbose:
			print 'All errors:', ponderatedErrors
		assert sum(importances) > 0
		avgErr = sum(errors) / sum(importances)
		if verbose:
			print 'Average error:', avgErr
			print ('Max error:', max(ponderatedErrors), 'Median error:',
				   sorted(ponderatedErrors)[len(errors) / 2])
		return avgErr, results

