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
        self.combo.activated.connect(self.drawRectangles)

        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Vlaggen")
        self.show()

    def drawRectangles(self,event):
        # bij het aangeklikte item wordt de bijhorende vlag random opgezocht
        #self.gekozen=self.combo.currentText()

        qp = QtGui.QPainter()
        qp.begin(self)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)

        qp.end()

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    ex=Interface()
    ex.show()
    app.exec_()