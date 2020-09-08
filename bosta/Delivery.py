
import os
import requests
import json
import logging

from bosta.utils.Address import *
from bosta.utils.Receiver import *
from bosta.utils.DeliverySpecs import *

with open(os.path.join(os.getcwd(),'bosta-python/bosta/config.json')) as configFile:
    config = json.load(configFile)

class Delivery:
    apiKey = os.getenv('BOSTA_API_KEY', '')
    
    @classmethod
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
    
    @classmethod
    def createDelivery(
       cls, deliveryType, dropOffAddress,
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
                "Authorization": cls.apiKey
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
