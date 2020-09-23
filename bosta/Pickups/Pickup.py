
import os
import logging
import requests

from bosta.ApiClient.ApiClient import BostaClient

from .ListAllPickupsRequest import ListAllPickupsRequest
from .ListAllPickupsResponse import ListAllPickupResponse

from .CreatePickupRequest import CreatePickupRequest 
from .CreatePickupResponse import CreatePickupResponse

from .GetPickupDetailsRequest import GetPickupDetailsRequest
from .GetPickupDetailsResponse import GetPickupDetailsResponse

from .UpdatePickupRequest import UpdatePickupRequest
from .UpdatePickupResponse import UpdatePickupResponse

from .DeletePickupRequest import DeletePickupRequest
from .DeletePickupResponse import DeletePickupResonse


class Pickup:
    def __init__(self):
        self.apiClient = BostaClient(
            os.environ.get('BOSTA_API_KEY'),
            os.environ.get('BOSTA_API_BASE')
        )
    
    def create(self, createPickupRequest: CreatePickupRequest)-> CreatePickupResponse:
        try:
            logging.info("Create New Pickup")
            url = self.apiClient.get_apiBase() + "pickups"
            headers = {
                "Authorization": self.apiClient.get_apiKey(),
                "content-type": "application/json"
            }
            response = requests.post(
                url,
                headers=headers,
                data=createPickupRequest.toJSONPayload()
            )
            if (response.status_code != 200): return response.text
            return CreatePickupResponse(response.json())
        
        except Exception as exp:
            logging.error(exp)
            raise exp

    def update(self, updatePickupRequest):
        try:
            logging.info("Update Pickup")
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = requests.put(
                self.apiClient.apiBase + "pickups/" + updatePickupRequest.get_id(),
                headers=headers,
                data=updatePickupRequest.toJSONPayload()
            )
            return UpdatePickupResponse(response)
        except Exception as exp:
            logging.error(exp)
            raise exp

    
    def listAll(self, listAllPickupsRequest):
        try:
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            params = listAllPickupsRequest.toQueryParams()
            response = requests.get(
                self.apiClient.apiBase + "pickups", 
                params= params, headers=headers
            )
            return ListAllPickupResponse(response.json())
        except Exception as exp:
            raise exp

    def get(self, getPickupDetailsRequest):
        try:
            logging.info("Get Pickup")

            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = requests.get(
                self.apiClient.apiBase + "pickups/" + getPickupDetailsRequest.get_id(),
                headers=headers
            )
            pickupObj = GetPickupDetailsResponse(response.json().message)
            return pickupObj
        except Exception as exp:
            logging.error(exp)
            raise exp
    
    def delete(self, deletePickupRequest):
        try:
            logging.info("Delete Pickup")

            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = requests.delete(
                self.apiClient.apiBase + "pickups/" + deletePickupRequest.get_id(),
                headers=headers
            )
            return DeletePickupResonse(response)
        except Exception as exp:
            logging.error(exp)
            raise exp


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
