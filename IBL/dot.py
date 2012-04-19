
class Dot:
	def __init__(self, position, clas=None):
		self.pos = position
		if clas != None:
			self.clas = clas

	def __str__(self):
		return str(self.clas)
