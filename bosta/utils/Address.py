class Address:
    def __init__(self, firstLine, secondLine, zone, city):
        self.firstLine = firstLine
        self.secondLine = secondLine
        self.city = {
            'name': city
        }
        self.zone = {
            'name': zone
        }

    def get_firstLine(self, street):
        return self.firstLine

    def get_secondLine(self, city):
        return self.city

    def get_city(self, state):
        return self.city

    def get_zone(self, zipcode):
        return self.zone

    def __str__(self):
        return str(self.firstLine,self.secondLine,self.city,self.zone)


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
