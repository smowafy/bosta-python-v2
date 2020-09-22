

class CreateDeliveryResponse:
    def __init__(self, jsonResponse):
        self.fromJSONPayload(jsonResponse)
    
    def fromJSONPayload(self, jsonResponse):
        self._id = jsonResponse["_id"]
        self.trackingNumber = jsonResponse["trackingNumber"]
        self.message = jsonResponse["message"]
    
    def get_deliveryId(self):
        return self._id

    def get_trackingNumber(self):
        return self.trackingNumber

    def get_message(self):
        return self.message

    def __str__(self):
        return self._id 
