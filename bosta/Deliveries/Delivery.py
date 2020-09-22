
import os
import requests
import json
import logging

from bosta.utils.Address import Address
from bosta.utils.Receiver import Receiver
from bosta.utils.DeliverySpecs import DeliverySpecs

from bosta.ApiClient.ApiClient import BostaClient

from .ListAllDeliveriesRequest import ListAllDeliveriesRequest 
from .ListAllDeliveriesResponse import ListAllDeliveriesResponse
from .UpdateDeliveryRequest import UpdateDeliveryRequest
from .UpdateDeliveryResponse import UpdateDeliveryResponse
from .PrintAWBRequest import PrintAWBRequest
from .PrintAWBResponse import PrintAWBResponse
from .TerminateDeliveryRequest import TerminateDeliveryRequest
from .TerminateDeliveryResponse import TerminateDeliveryResponse
from .CreateDeliveryRequest import CreateDeliveryRequest
from .CreateDeliveryResponse import CreateDeliveryResponse

class Delivery:

    def __init__(self):
        self.apiClient = BostaClient(
            os.environ.get('BOSTA_API_KEY'),
            os.environ.get('BOSTA_API_BASE')
        )

    def listAll(self, listAllDeliveriesRequest: ListAllDeliveriesRequest)-> ListAllDeliveriesResponse:
        try:
            logging.info("list all business deliveries")
            url = self.apiClient.apiBase + "deliveries" 
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            params = listAllDeliveriesRequest.toUrlQueryParamters()
            response = requests.get(url, params = params, headers=headers)
            if (response.status_code) != 200: return response.text.message
            instance = ListAllDeliveriesResponse(response.json())
            return instance
        except Exception as exp:
            logging.error(exp)
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
    
    
    def create(self, createDeliveryRequest: CreateDeliveryRequest)-> CreateDeliveryResponse:
        try:
            payload = createDeliveryRequest.toJSONPayload()
            logging.info('Create New Delivery: Payload '+ str(payload))
            url = self.apiClient.get_apiBase() + "deliveries"
            headers = {
                "Authorization": self.apiClient.get_apiKey(),
                "content-type": "application/json"
            }
            response = requests.post(url, headers=headers, data=payload)
            if (response.status_code) != 201: return response.text
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
    

if __name__ == 'bosta.Delivery' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
