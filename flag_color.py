#!/usr/bin/env python

from PyQt4 import QtGui

from random import randrange

"""This class generates a random flagcolor for a country"""

class FlagColor(QtGui.QColor):
    def __init__(self):
        """Sets color for a flag"""
        super(FlagColor,self).__init__()
        self.genColors()

    def genColors(self):
        """Creates a random color for a flag"""
        self.setRed(randrange(0,256))
        self.setGreen(randrange(0,256))
        self.setBlue(randrange(0,256))
        
if __name__== "__main__":
    main()
