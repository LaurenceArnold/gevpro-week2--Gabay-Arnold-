#!/usr/bin/env python

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
		
		self.combo = QtGui.QComboBox(self)
		self.combo.move(5, 50)
		self.combo.resize(120,30)
		
		lijst=[]
		with open('countries_list.txt') as in_f:
			for line in in_f:
				x = line.split('\n')
				lijst.append(x)
		lijst2=[]
		for i in lijst:
			lijst2.append(i[0])				
		self.combo.addItems(lijst2)
		#self.combo.activated.connect(self.paintEvent)
		
		self.countryDic={}
		for country in lijst2:
			self.countryDic[country]=country		
		
		self.setGeometry(200,200,300,300)
		self.setWindowTitle("Vlaggen bij een Land!")
		self.show()		

	def paintEvent(self, event):
		#activates a pain-Event
		qp = QtGui.QPainter()
		qp.begin(self)
		for country in self.countryDic:
			qp.setBrush(QtGui.QColor(randrange(0,256,1),randrange(0,256,1), randrange(0,256,1)))
			qp.drawRect(10, 80, 90, 60)
			self.countryDic[country]=self.countryDic[country], qp
		
		qp.end()
	
	#def drawRectangles(self,event,qp):						
		
		#print(self.countryDic)
		
	
if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    interface=Interface()
    interface.show()
    app.exec_()
