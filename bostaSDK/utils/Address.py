from typing import Optional

class Address:
    def __init__(
        self, city: str, firstLine: str, districtId: str,
        secondLine: str, buildingNumber: int, floor: int,
        apartment: int, isWorkAddress: bool=False,
        zoneId: Optional[str]=None
    ):
        """ Initialize new instance from Address class

        Parameters:
        city (str)
        firstLine (str)
        districtId (str)
        secondLine (str)
        buildingNumber (int)
        floor (int)
        apartment (int)
        isWorkAddess (bool) [optional]
        zoneId (str) [optional]

        Returns: New instance from Address class
        """
        self.city = city
        self.firstLine = firstLine
        self.zoneId = zoneId
        self.secondLine = secondLine
        self.districtId = districtId
        self.buildingNumber = buildingNumber
        self.floor = floor
        self.apartment = apartment
        self.isWorkAddress = isWorkAddress

    def get_firstLine(self):
        return self.firstLine

    def get_secondLine(self):
        return self.secondLine

    def get_city(self):
        return self.city

    def get_zoneId(self):
        return self.zoneId

    def get_districtId(self):
        return self.districtId

    def toJSON(self):
        """
        Returns:
        JSON object from current instance

        """
        addressObj = {
            "city": self.city,
            "firstLine": self.firstLine,
            "districtId": self.districtId,
            "isWorkAddress": self.isWorkAddress,
            "secondLine": self.secondLine,
            "buildingNumber": self.buildingNumber,
            "floor": self.floor,
            "apartment": self.apartment
        }
        if self.zoneId is not None:
            addressObj["zoneId"] = self.zoneId

        return addressObj


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
