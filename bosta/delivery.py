
import os
import requests
import json
import logging

from bosta.utils.Address import *
from bosta.utils.Receiver import *
from bosta.utils.DeliverySpecs import *

with open('config.json') as configFile:
    config = json.load(configFile)

class Delivery:
    def __init__(self):
        self.apiKey = os.getenv('BOSTA_API_KEY', '')

    def getBusinessDeliveries(self):
        try:
            headers = {
                "Authorization": self.apiKey
            }
            response = requests.get(config['BOSTA_URL'] + "deliveries", headers=headers)
            return response.json()
        except Exception as exp:
            raise exp

    def getDeliveriesSummary(self):
        try:
            headers = {
                "Authorization": self.apiKey
            }
            response = requests.get(config['BOSTA_URL']+ "deliveries/in-progress/summary", headers=headers)
            return response.json
        except Exception as exp:
            raise exp

    def getAirwayBill(self, ids):
        try:
            headers = {
                "Authorization": self.apiKey
            }
            response = requests.get(config['BOSTA_URL']+ "deliveries/awb?ids="+ids, headers=headers)
            return response.json
        except Exception as exp:
            raise exp
    
    def createDelivery(
       self, deliveryType, dropOffAddress,
       receiver, cashOnDelivery, specs,
    ):
        """Create new delivery authenticated by business api key

        Parameters:
        deliveryType (int)
        specs (DeliverySpecs)
        dropOffAddress (Address)
        cashOnDelivery (int): cash on delivert amount
        receiver (Receiver)

  
        Returns:
        object:Returning new delivery tracking number

        """
        try:
            logging.info('Create New Delivery')
            headers = {
                "Authorization": self.apiKey
            }
            payload = {     
                "type": deliveryType,
                "specs": specs,
                "cod": cashOnDelivery,
                "dropOffAddress": dropOffAddress,
                "receiver": receiver,
            }
            response = requests.post(config['BOSTA_URL'] + "deliveries", headers=headers, payload=payload)
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp


    

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
