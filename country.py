#!/usr/local/bin/python3

class Country:
    def __init__(self,country):
        self.country=country

    def getCountry(self):
        return self.country

    def __str__(self):
        return ("Hello from {} ".format(self.country))

if __name__== "__main__":
    main()