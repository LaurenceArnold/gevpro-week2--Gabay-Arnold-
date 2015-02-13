#!/opt/local/bin/python3.4

from PyQt4 import QtGui

from random import randrange

class FlagColor(QtGui.QColor):
    def __init__(self):
        super(FlagColor,self).__init__()

    def kleurvlag(self,getal):
        if getal == 0:
            self.setRed()
        if getal == 1:
            self.setGreen()
        if getal == 2:
            self.setBlue()

if __name__== "__main__":
    main()


