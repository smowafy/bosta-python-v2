
import os
import logging
import requests

from bosta.ApiClient import ApiClient

from .CreatePickupRequest import CreatePickupRequest 
from .CreatePickupResponse import CreatePickupResponse
from .GetPickupDetailsRequest import GetPickupDetailsRequest
from .GetPickupDetailsResponse import GetPickupDetailsResponse
from .ListAllPickupsRequest import ListAllPickupsRequest
from .ListAllPickupsResponse import ListAllPickupResponse
from .UpdatePickupRequest import UpdatePickupRequest
from .UpdatePickupResponse import UpdatePickupResponse
from .DeletePickupRequest import DeletePickupRequest
from .DeletePickupResponse import DeletePickupResonse


class Pickup:
    def __init__(self):
        self.apiClient = ApiClient(
            os.getenv('BOSTA_API_KEY', ''),
            os.getenv('BOSTA_API_BASE', ''),
        )
    
    def create(self, createPickupRequest):
        try:
            logging.info("Create New Pickup")
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = requests.post(
                self.apiClient.apiBase + "pickups",
                headers=headers,
                payload=createPickupRequest.toJsonPayload()
            )
            instance = CreatePickupResponse(response.json())
            return instance.fromJsonPayload()
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
                payload=updatePickupRequest.toJsonPayload()
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
