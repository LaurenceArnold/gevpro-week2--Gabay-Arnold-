#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

from random import randrange
from country import *

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
		
		self.countryDic={}
		for country in lijst2:
			self.countryDic[country]=Country(country)		
		
		self.setGeometry(200,200,300,300)
		self.setWindowTitle("Vlaggen bij een Land!")
		self.frame = QtGui.QFrame(self)
		self.frame.move(5,90)
		self.frame.resize(120,80)
		self.frame.setStyleSheet("QFrame {background-color: yellow} ")
		self.show()		

	
	
if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    interface=Interface()
    interface.show()
    app.exec_()
