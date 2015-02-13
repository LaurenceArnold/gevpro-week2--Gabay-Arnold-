#!/opt/local/bin/python3.4

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
        #self.combo.activated.connect(self.alterLCD)

        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Vlaggen")
        self.show()

    #def alterLCD(self):
        # bij het aangeklikte item wordt de bijhorende vlag random opgezocht
        #self.gekozen=self.combo.currentText()

        #self.flag= QtGui.QFrame.QRect(30, 10, 100, 50)
        #self.setStyleSheet("self.combo {color:red}");

        #self.flag.setStyleSheet("QFrame{ background-color: yellow }");

        #setStyleSheet("self.flag { background-color: yellow }" % self.flag.name())

        #Als je een QFrame-object gebruikt om de flag te tonen, kan je deze methode gebruiken om
        # een bepaalde kleur te laten zien:
       # setStyleSheet("QFrame { background-color: %s }" % flag_colour.name())

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    ex=Interface()
    ex.show()
    app.exec_()