#!/usr/bin/env python
import sys
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import QtGui, QtCore
from PyQt4.uic import *
f = open('mimi.py', 'w')
compileUi('untitled.ui', f)
f.close()
from mimi import Ui_Dialog
###
class MyView(QtGui.QGraphicsView):
	def __init__(self):
		QtGui.QGraphicsView.__init__(self)

		self.scene = QtGui.QGraphicsScene(self)
		self.scene.setSceneRect(QtCore.QRectF(0, 0, 400, 400))

		self.setScene(self.scene)

		self.item = QtGui.QGraphicsEllipseItem(0, 0, 60, 40)
		self.scene.addItem(self.item)


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	view = MyView()
	view.show()
	sys.exit(app.exec_())
###
'''
app = QApplication(sys.argv)
window = QDialog()

ui = Ui_Dialog()
ui.setupUi(window)


window.show()

sys.exit(app.exec_())
'''
