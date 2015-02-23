#!/usr/bin/env python

from flag_color import *

"""This class creates a Country with a random generated flag"""
class Country:
    def __init__(self,country):
        """Creates a Countryobject"""
        self.country=country
        self.flag=FlagColor()

    def getCountry(self):
        """returns name of the countryobject"""
        return self.country

    def displayFlag(self):
        return self.flag

    def __str__(self):
        return ("Hello from {} ".format(self.country))

if __name__== "__main__":
    main()
