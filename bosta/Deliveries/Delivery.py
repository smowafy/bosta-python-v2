
import os
import requests
import json
import logging

from bosta.utils.Address import Address
from bosta.utils.Receiver import Receiver
from bosta.utils.DeliverySpecs import DeliverySpecs

from .ListAllDeliveriesRequest import ListAllDeliveriesRequest
from .ListAllDeliveriesResponse import ListAllDeliveriesResponse

from .UpdateDeliveryRequest import UpdateDeliveryRequest
from .UpdateDeliveryResponse import  UpdateDeliveryResponse

from .PrintAWBRequest import PrintAWBRequest
from .PrintAWBResponse import PrintAWBResponse

from .TerminateDeliveryRequest import TerminateDeliveryRequest
from .TerminateDeliveryResponse import TerminateDeliveryResponse

from .CreateDeliveryRequest import CreateDeliveryRequest
from .CreateDeliveryResponse import CreateDeliveryResponse


class Delivery:

    def __init__(self, apiClient):
        self.apiClient = apiClient

    def listAll(self, listAllDeliveriesRequest: ListAllDeliveriesRequest):
        try:
            logging.info("list all business deliveries")
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = requests.get(
                self.apiClient.apiBase + "deliveries" + listAllDeliveriesRequest.toUrlQueryParamters(), 
                headers=headers
            )
            return ListAllDeliveriesResponse(response.json())
        except Exception as exp:
            raise exp
    

    def printAirWayBill(self, printAWBRequest: PrintAWBRequest):
        try:
            logging.info("Print airway bill")
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = requests.get(
                self.apiClient.apiBase + "deliveries/awb?" + printAWBRequest.toUrlQueryParamters(), 
                headers=headers
            )
            return PrintAWBResponse(response.json())
        except Exception as exp:
            raise exp
    
    
    def create(self, createDeliveryRequest: CreateDeliveryRequest):
        try:
            logging.info('Create New Delivery')
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            payload = createDeliveryRequest.toJSONPayload()
            response = requests.post(
                self.apiClient.apiBase + "deliveries",
                headers=headers, payload=payload
            )
            return CreateDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def update(self, updateDeliveryRequest: UpdateDeliveryRequest):
        try:
            logging.info('Update Delivery')
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            payload = updateDeliveryRequest.toJSONPayload()
            response = requests.patch(
                self.apiClient.apiBase + "deliveries" + updateDeliveryRequest.get_deliveryId(),
                headers=headers, payload=payload
            )
            return UpdateDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def terminate(self, terminateDeliveryRequest: TerminateDeliveryRequest):
        try:
            logging.info("list all business deliveries")
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = requests.delete(
                self.apiClient.apiBase + "deliveries/" + terminateDeliveryRequest.get_deliveryId(), 
                headers=headers
            )
            return TerminateDeliveryResponse(response.json())
        except Exception as exp:
            raise exp
    

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
