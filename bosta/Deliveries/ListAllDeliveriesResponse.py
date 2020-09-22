
import logging

class ListAllDeliveriesResponse:
    def __init__(self, jsonPayload):
        self.deliveries, self.count = self.fromJSONPayload(jsonPayload)
    
    def fromJSONPayload(self, jsonPayload):
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
