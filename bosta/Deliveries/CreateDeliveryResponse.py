

class CreateDeliveryResponse:
    def __init__(self, jsonResponse):
        self.fromJsonPayload(jsonResponse)
    
    def fromJsonPayload(self, jsonResponse):
        self._id = jsonResponse["_id"]
        self.trackingNumber = jsonResponse["trackingNumber"]
        self.message = jsonResponse["message"]
