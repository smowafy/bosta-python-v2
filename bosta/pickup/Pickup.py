
import os
import logging

from bosta.apiClient.ApiClient import ApiClient

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
    def __init__(self, apiClient):
        self.apiClient = apiClient
    
    def create(self, createPickupRequest: CreatePickupRequest)-> CreatePickupResponse:
        """
        Create New Pickup.

        Parameters:
        createPickupRequest (CreatePickupRequest)

        Returns: New instance from CreatePickupResponse.   
        """
        try:
            logging.info("Create New Pickup")
            url = self.apiClient.get_apiBase() + "pickups"
            headers = {
                "Authorization": self.apiClient.get_apiKey(),
                "content-type": "application/json"
            }
            response = self.apiClient.send('post',
                url,
                headers=headers,
                data=createPickupRequest.toJSONPayload()
            )
            if (response.status_code != 200): return response.text
            return CreatePickupResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def update(self, updatePickupRequest: UpdatePickupRequest) -> UpdatePickupResponse:
        """
        Update Pickup.

        Parameters:
        updatePickupRequest (UpdatePickupRequest)

        Returns: New instance from UpdatePickupResponse.   
        """
        try:
            logging.info("Update Pickup")
            url = self.apiClient.get_apiBase() + "pickups/" + str(updatePickupRequest.get_id())
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = self.apiClient.send(
                'put',
                url,
                headers=headers,
                data=updatePickupRequest.toJSONPayload()
            )
            if (response.status_code != 200): return response.text
            return UpdatePickupResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    
    def listAll(self, listAllPickupsRequest: ListAllPickupsRequest) -> ListAllPickupResponse:
        """
        List All Pickup.

        Parameters:
        listAllPickupsRequest (ListAllPickupsRequest)

        Returns: New instance from ListAllPickupResponse.   
        """
        try:
            url = self.apiClient.apiBase + "pickups"
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            params = listAllPickupsRequest.toQueryParamters()
            response = self.apiClient.send('get',url, params= params, headers=headers)
            if (response.status_code != 200): return response.text
            return ListAllPickupResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

    def get(self, getPickupDetailsRequest: GetPickupDetailsRequest) -> GetPickupDetailsResponse:
        """
        Get Pickup.

        Parameters:
        getPickupDetailsRequest (GetPickupDetailsRequest)

        Returns: New instance from GetPickupDetailsResponse.   
        """
        try:
            logging.info("Get Pickup")
            url = self.apiClient.get_apiBase() + "pickups/" + str(getPickupDetailsRequest.get_pickupId())
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            response = self.apiClient.send('get',url, headers=headers)
            if (response.status_code != 200): return response.text
            return GetPickupDetailsResponse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp
    
    def delete(self, deletePickupRequest: DeletePickupRequest) -> DeletePickupResonse:
        """
        Delete Pickup.

        Parameters:
        deletePickupRequest (DeletePickupRequest)

        Returns: New instance from DeletePickupResonse.   
        """
        try:
            logging.info("Delete Pickup")
            url = self.apiClient.apiBase + "pickups/" + str(deletePickupRequest.get_pickupId())
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = self.apiClient.send('delete',url,headers=headers)
            if (response.status_code != 200): return response.text
            return DeletePickupResonse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

