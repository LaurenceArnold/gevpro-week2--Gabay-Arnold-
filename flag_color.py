#!/opt/local/bin/python3.4

from PyQt4 import QtGui

from random import randrange

class FlagColor(QtGui.QColor):
    def __init__(self):
        super(FlagColor,self).__init__()

    def kleurvlag(self):
		self.setRed(randrange(0,256))
		self.setGreen(randrange(0,256))
		self.setBlue(randrange(0,256))
		
		return self.SetRed,self.setGreen,self.setBlue
		
        
if __name__== "__main__":
    main()
