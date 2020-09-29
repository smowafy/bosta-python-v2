
import os
import json
import logging

from bosta.utils.Address import Address
from bosta.utils.Receiver import Receiver
from bosta.utils.DeliverySpecs import DeliverySpecs


from .list.ListAllDeliveriesRequest import ListAllDeliveriesRequest 
from .list.ListAllDeliveriesResponse import ListAllDeliveriesResponse
from .update.UpdateDeliveryRequest import UpdateDeliveryRequest
from .update.UpdateDeliveryResponse import UpdateDeliveryResponse
from .printAWB.PrintAWBRequest import PrintAWBRequest
from .printAWB.PrintAWBResponse import PrintAWBResponse
from .terminate.TerminateDeliveryRequest import TerminateDeliveryRequest
from .terminate.TerminateDeliveryResponse import TerminateDeliveryResponse
from .create.CreateDeliveryRequest import CreateDeliveryRequest
from .create.CreateDeliveryResponse import CreateDeliveryResponse
from .track.TrackDeliveryRequest import TrackDeliveryRequest
from .track.TrackDeliveryResponse import TrackDeliveryResponse

class Delivery:

    def __init__(self, apiClient):
        self.apiClient = apiClient

    def listAll(self, listAllDeliveriesRequest: ListAllDeliveriesRequest)-> ListAllDeliveriesResponse:
        """
        List All Deliveries.

        Parameters:
        listAllDeliveriesRequest (ListAllDeliveriesRequest)

        Returns: New instance from ListAllDeliveriesResponse.   
        """
        try:
            logging.info("list all business deliveries")
            url = self.apiClient.get_apiBase() + "api/v0/deliveries" 
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            params = listAllDeliveriesRequest.toUrlQueryParamters()
            response = self.apiClient.send('get', url, params = params, headers=headers)
            if (response.status_code) != 200: return response.text.message
            instance = ListAllDeliveriesResponse(response.json())
            return instance
        except Exception as exp:
            logging.error(exp)
            raise exp
    

    def printAirWayBill(self, printAWBRequest: PrintAWBRequest) -> PrintAWBResponse:
        """
        Print Delivery Airway Bill.

        Parameters:
        printAWBRequest (PrintAWBRequest)

        Returns: New instance from PrintAWBResponse.   
        """
        try:
            logging.info("Print airway bill")
            url = self.apiClient.get_apiBase() + "api/v0/deliveries/awb" 
            params = printAWBRequest.toUrlQueryParamters()
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = self.apiClient.send('get',url, params=params, headers=headers)
            if (response.status_code) != 200: return response.text.message
            return PrintAWBResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp
    
    
    def create(self, createDeliveryRequest: CreateDeliveryRequest)-> CreateDeliveryResponse:
        """
        Create New Delivery.

        Parameters:
        createDeliveryRequest (CreateDeliveryRequest)

        Returns: New instance from CreateDeliveryResponse.   
        """
        try:
            payload = createDeliveryRequest.toJSONPayload()
            logging.info('Create New Delivery: Payload '+ str(payload))
            url = self.apiClient.get_apiBase() + "api/v0/deliveries"
            headers = {
                "Authorization": self.apiClient.get_apiKey(),
                "content-type": "application/json"
            }
            response = self.apiClient.send('post',url, headers=headers, data=payload)
            if (response.status_code) != 201: return response.text
            return CreateDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def update(self, updateDeliveryRequest: UpdateDeliveryRequest)->  UpdateDeliveryResponse:
        """
        Update Delivery.

        Parameters:
        updateDeliveryRequest (UpdateDeliveryRequest)

        Returns: New instance from UpdateDeliveryResponse.   
        """
        try:
            logging.info('Update Delivery')
            url = self.apiClient.get_apiBase() + "api/v0/deliveries/" + str(updateDeliveryRequest.get_deliveryId())
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            payload = updateDeliveryRequest.toJSONPayload()
            response = self.apiClient.send('patch',url, headers=headers, data=payload)
            if (response.status_code) != 200: return response.text
            return UpdateDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def terminate(self, terminateDeliveryRequest: TerminateDeliveryRequest)-> TerminateDeliveryResponse:
        """
        Terminate Delivery.

        Parameters:
        terminateDeliveryRequest (TerminateDeliveryRequest)

        Returns: New instance from TerminateDeliveryResponse.   
        """
        try:
            logging.info("Terminate Delivery")
            url = self.apiClient.get_apiBase() + "api/v0/deliveries/" + str(terminateDeliveryRequest.get_deliveryId())

            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = self.apiClient.send('delete',url,headers=headers)
            if (response.status_code) != 200: return response.text
            return TerminateDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def track(self, trackDeliveryRequest: TrackDeliveryRequest)-> TrackDeliveryResponse:
        """
        Track Delivery.

        Parameters:
        trackDeliveryRequest (TrackDeliveryRequest)

        Returns: New instance from TrackDeliveryResponse.   
        """
        try:
            logging.info('Track Delivery')
            url = self.apiClient.get_apiBase() + "api/v0/deliveries/" + str(trackDeliveryRequest.get_deliveryId()) + "/state-history"
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = self.apiClient.send('get',url, headers=headers)
            if (response.status_code) != 200: return response.text
            return TrackDeliveryResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    