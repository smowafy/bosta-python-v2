
import logging

class ListAllDeliveriesResponse:
    def __init__(self, jsonPayload):
        """ Initialize new instance from ListAllDeliveriesResponse class

        Parameters:
        jsonPayload (dict): JSON response object
  
        Returns: instance from ListAllDeliveriesResponse

        """
        self.deliveries, self.count = self.fromJSONPayload(jsonPayload)
    
    def fromJSONPayload(self, jsonPayload):
        """ 
        Extract deliveries and count fields from json response object

        Parameters: 
        jsonResponse (dict): JSON response object 
        
        Returns: 
        deliveries (array): List of deliveries 
        count (int): Number of deliveries in list
        """  
        try:
            data = jsonPayload
            deliveries = []
            for delivery in data["deliveries"]:
                deliveries.append(delivery)
            count = jsonPayload["count"]
            return deliveries, count 
        except Exception as exp:
            raise exp

    def get_deliveries(self): 
        return self.deliveries
    def get_count(self):
        return self.count
