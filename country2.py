#!/usr/local/bin/python3

from flag_color import *


class Country:
    def __init__(self,country):
        self.country=country
        self.flag=flag
        getal=flag_color()

    def getCountry(self):
        return self.country

    def displayFlag(self,getal):
        getal=randrange(0,3)
        self.flag(getal)

    def __str__(self):
        return ("Hello from {} ".format(self.country))

if __name__== "__main__":
    main()