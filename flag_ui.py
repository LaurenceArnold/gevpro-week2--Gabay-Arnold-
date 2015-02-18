#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

from random import randrange
from country2 import *
from flag_color import *

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
		#countryObjList = []
		#for country in lijst2:
			#countryObjList.append(Country(country,FlagColor())
			
		self.setGeometry(200,200,300,300)
		self.setWindowTitle("Vlaggen bij een Land!")
		self.frame = QtGui.QFrame(self)
		self.frame.move(5,90)
		self.frame.resize(120,80)
		self.show()
		self.MakeFlag()
		self.combo.activated.connect(self.MakeFlag)
		
	def MakeFlag(self):
		choosenCountry = self.combo.currentText()
		countryObj = Country(choosenCountry)
		flag_color = countryObj.displayFlag()
		self.frame.setStyleSheet("QFrame {background-color: %s}" %flag_color.name())
	
	
if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    interface=Interface()
    interface.show()
    app.exec_()
