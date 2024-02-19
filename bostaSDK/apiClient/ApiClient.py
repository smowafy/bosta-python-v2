import requests

from ..delivery import Delivery
from ..pickup import Pickup

from ..city import City
from ..district import District

from ..utils import DELIVERY_TYPES
from ..utils import PICKUP_TIME_SLOTS


class ApiClient:
    def __init__(self, apiKey, apiBase="https://app.bosta.co"):
        """
        Initialize new instance from apiClient class

        Parameters:
        apiKey (string): Business api key
        apiBase (string): Bosta host url

        Returns:
        apiClient: instance from apiClient

        """
        self.apiKey = apiKey
        self.apiBase = apiBase
        self.pickup = Pickup(self)
        self.delivery = Delivery(self)
        self.cities = City(self)
        self.districts = District(self)
        self.deliveyTypes = DELIVERY_TYPES
        self.pickupTimeSlots = PICKUP_TIME_SLOTS


        self.citiesAll = City(self).listAll()
        self.districtsAll = District(self).listAll()

        self.EGYPT_COUNTRY_ID = '60e4482c7cb7d4bc4849c4d5'
        self.KSA_COUNTRY_ID = 'eF-3f9FZr'

        self.countries = [
            {
                "id": self.EGYPT_COUNTRY_ID,
                "name": "Egypt"
            },
            {
                "id": self.KSA_COUNTRY_ID,
                "name": "Kingdom of Saudi Arabia"
            }
        ]

    def get_apiKey(self): return self.apiKey
    def get_apiBase(self): return self.apiBase
    def get_delivery(self): return self.delivery
    def get_pickup(self): return self.pickup
    def get_cities(self): return self.citiesAll

    def send(self, method, url, headers={}, params=None, data=None):
        try:
            """
            Send HTTP Request

            Parameters:
            method (string): Request method type
            url (string): Full url path
            headers (dict): Request headers
            params (dict): Request parameters
            data (dict): Request payload data

            Returns:
            response: Http response object

            """
            headers['X-Requested-By'] = 'python-sdk'
            headers['Authorization'] = self.apiKey
            url = self.apiBase + "/api/v2" + url
            return getattr(requests, method)(
                url, headers=headers, params=params, data=data
            )
        except Exception as exp:
            raise exp


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
