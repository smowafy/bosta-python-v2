
import os
import requests
import json
import logging

from bosta.utils.Address import *
from bosta.utils.Receiver import *
from bosta.utils.DeliverySpecs import *

from .CreateDeliveryRequest import CreateDeliveryRequest
from .CreateDeliveryResponse import CreateDeliveryResponse

class Delivery:

    def __init__(self, apiClient):
        self.apiClient = apiClient

    def getBusinessDeliveries(cls):
        try:
            headers = {
                "Authorization": cls.apiKey
            }
            response = requests.get(config['BOSTA_URL'] + "deliveries", headers=headers)
            return response.json()
        except Exception as exp:
            raise exp
    
    @classmethod
    def getDeliveriesSummary(cls):
        try:
            headers = {
                "Authorization": cls.apiKey
            }
            response = requests.get(config['BOSTA_URL']+ "deliveries/in-progress/summary", headers=headers)
            return response.json()
        except Exception as exp:
            raise exp

    @classmethod
    def getAirwayBill(cls, ids):
        try:
            headers = {
                "Authorization": cls.apiKey
            }
            response = requests.get(config['BOSTA_URL']+ "deliveries/awb?ids="+ids, headers=headers)
            return response.json()
        except Exception as exp:
            raise exp
    
    
    def createDelivery(self, createDeliveryRequest):

        try:
            logging.info('Create New Delivery')
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            payload = createDeliveryRequest.toJSONPayload()
            response = requests.post(
                self.apiClient['BOSTA_URL'] + "deliveries",
                headers=headers, payload=payload
            )
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp


    

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
