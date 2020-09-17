
import json

class ListAllDeliveriesResponse:
    def __init__(self, jsonPayload):
        self.deliveries, self.count = self.fromJsonPayload(jsonPayload)
    
    def fromJsonPayload(self, jsonPayload):
        data = json.load(jsonPayload)
        deliveries = []
        for delivery in data["deliveries"]:
            deliveries.append(delivery)
        count = jsonPayload["count"]
        return {deliveries, count }
