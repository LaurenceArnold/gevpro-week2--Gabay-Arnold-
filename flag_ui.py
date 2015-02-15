#!/opt/local/bin/python3.4
#voor linux
#!usr/bin/env python


from PyQt4 import QtGui, QtCore

from random import randrange

import sys

class Interface(QtGui.QWidget):

	def __init__(self):
		super(Interface,self).__init__()
		self.initUI()

	def initUI(self):
		#button 1
		self.btn=QtGui.QLabel('Land',self)
		self.btn.move(30,30)

		#dropdownmenu
		self.combo = QtGui.QComboBox(self)
		self.combo.move(5, 50)
		self.combo.resize(120,30)

		# hier wordt het dropdownmenu gemaakt via een list
		# lege lijst en alle items appenden, deze lijst adden
		lijst=[]
		with open('countries_list.txt') as in_f:
			for line in in_f:
				x = line.split('\n')
				lijst.append(x)

		lijst2=[]
		for i in lijst:
			lijst2.append(i[0])
		print(lijst2)
		self.combo.addItems(lijst2)
		self.combo.activated.connect(self.paintEvent)

		self.setGeometry(200,200,300,300)
		self.setWindowTitle("Vlaggen")
		self.show()

	def paintEvent(self, e):
		#activates a pain-Event
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self, qp):
		#Choose random color and paint flag
		qp.setBrush(QtGui.QColor(randrange(0,256,1),randrange(0,256,1), randrange(0,256,1)))
		qp.drawRect(10, 80, 90, 60)

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    ex=Interface()
    ex.show()
    app.exec_()
