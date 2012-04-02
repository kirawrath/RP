#!/usr/bin/env python
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QPointF
from PyQt4.QtGui import QApplication, QDialog,\
QGraphicsPolygonItem, QPolygonF

class MyView(QtGui.QGraphicsView):
	def __init__(self):
		self.gview = QtGui.QGraphicsView.__init__(self)

		self.scene = QtGui.QGraphicsScene(self)
		self.scene.setSceneRect(QtCore.QRectF(0, 0, 400, 400))

		self.setScene(self.scene)

	def draw_polygon(self, dots):
		polygon = QPolygonF(map(lambda a: QPointF(a[0],a[1]), dots))

		poly_item = QGraphicsPolygonItem(polygon,self.gview,self.scene)

class Interface:
	def __init__(self, argv):
		self.app = QtGui.QApplication(argv)
		self.view = MyView()
		self.view.show()
	
	#dots = [(,),(,),(,)]
	def add_polygon(self,dots):
		self.view.draw_polygon(dots)
	
	def show(self):
		sys.exit(self.app.exec_())

if __name__ == '__main__':
	ui = Interface(sys.argv)
	dots = [(0,0),(50,50),(100,25)]
	ui.add_polygon(dots)
	ui.show()
