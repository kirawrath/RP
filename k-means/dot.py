
class Dot:
	def __init__(self, position, clas=None):
		self.pos = position
		self.clas = clas
		if clas != None:
			self.clas = clas

	def __str__(self):
		return 'c: '+str(self.clas)+', '+str(self.pos)

	def __len__(self):
		return len(self.pos)
