
class UpdateDeliveryResponse:

    def __init__(self, jsonPayload):
        self.fromJsonPayload(jsonPayload)
    
    def fromJsonPayload(self, jsonPayload):
        self.message = jsonPayload["message"]
        self._id = jsonPayload["_id"]
