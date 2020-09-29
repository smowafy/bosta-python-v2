
import os
import logging


from .list.ListAllPickupsRequest import ListAllPickupsRequest
from .list.ListAllPickupsResponse import ListAllPickupResponse

from .create.CreatePickupRequest import CreatePickupRequest 
from .create.CreatePickupResponse import CreatePickupResponse

from .get.GetPickupDetailsRequest import GetPickupDetailsRequest
from .get.GetPickupDetailsResponse import GetPickupDetailsResponse

from .update.UpdatePickupRequest import UpdatePickupRequest
from .update.UpdatePickupResponse import UpdatePickupResponse

from .delete.DeletePickupRequest import DeletePickupRequest
from .delete.DeletePickupResponse import DeletePickupResonse


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
            url = self.apiClient.get_apiBase() + "api/v0/pickups"
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
            url = self.apiClient.get_apiBase() + "api/v0/pickups/" + str(updatePickupRequest.get_id())
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
            url = self.apiClient.apiBase + "api/v0/pickups"
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
            url = self.apiClient.get_apiBase() + "api/v0/pickups/" + str(getPickupDetailsRequest.get_pickupId())
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
            url = self.apiClient.apiBase + "api/v0/pickups/" + str(deletePickupRequest.get_pickupId())
            headers = {
                "Authorization": self.apiClient.apiKey
            }
            response = self.apiClient.send('delete',url,headers=headers)
            if (response.status_code != 200): return response.text
            return DeletePickupResonse(response.json())
        except Exception as exp:
            logging.error(exp)
            raise exp

