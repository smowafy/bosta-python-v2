
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
from .TrackDeliveryRequest import TrackDeliveryRequest
from .TrackDeliveryResponse import TrackDeliveryResponse

class Delivery:

    def __init__(self):
        self.apiClient = BostaClient(
            os.environ.get('BOSTA_API_KEY'),
            os.environ.get('BOSTA_API_BASE')
        )

    def listAll(self, listAllDeliveriesRequest: ListAllDeliveriesRequest)-> ListAllDeliveriesResponse:
        try:
            logging.info("list all business deliveries")
            url = self.apiClient.get_apiBase() + "deliveries" 
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            params = listAllDeliveriesRequest.toUrlQueryParamters()
            response = requests.get(url, params = params, headers=headers)
            if (response.status_code) != 200: return response.text.message
            instance = ListAllDeliveriesResponse(response.json())
            return instance
        except Exception as exp:
            logging.error(exp)
            raise exp
    

    def printAirWayBill(self, printAWBRequest: PrintAWBRequest) -> PrintAWBResponse:
        try:
            logging.info("Print airway bill")
            url = self.apiClient.get_apiBase() + "deliveries/awb" 
            params = printAWBRequest.toUrlQueryParamters()
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = requests.get(url, params=params, headers=headers)
            if (response.status_code) != 200: return response.text.message
            return PrintAWBResponse(response.json())
        except Exception as exp:
            logging.error(exp)
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

    def update(self, updateDeliveryRequest: UpdateDeliveryRequest)->  UpdateDeliveryResponse:
        try:
            logging.info('Update Delivery')
            url = self.apiClient.get_apiBase() + "deliveries/" + str(updateDeliveryRequest.get_deliveryId())
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            payload = updateDeliveryRequest.toJSONPayload()
            response = requests.patch(url, headers=headers, data=payload)
            if (response.status_code) != 200: return response.text
            return UpdateDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def terminate(self, terminateDeliveryRequest: TerminateDeliveryRequest)-> TerminateDeliveryResponse:
        try:
            logging.info("Terminate Delivery")
            url = self.apiClient.get_apiBase() + "deliveries/" + str(terminateDeliveryRequest.get_deliveryId())

            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = requests.delete(url,headers=headers)
            if (response.status_code) != 200: return response.text
            return TerminateDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def track(self, trackDeliveryRequest: TrackDeliveryRequest)-> TrackDeliveryResponse:
        try:
            logging.info('Track Delivery')
            url = self.apiClient.get_apiBase() + "deliveries/" + str(trackDeliveryRequest.get_deliveryId()) + "/state-history"
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = requests.get(url, headers=headers)
            if (response.status_code) != 200: return response.text
            return TrackDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    