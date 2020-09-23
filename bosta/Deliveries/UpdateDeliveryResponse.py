
class UpdateDeliveryResponse:

    def __init__(self, jsonPayload):
        self.fromJSONPayload(jsonPayload)
    
    def fromJSONPayload(self, jsonPayload):
        self.message = jsonPayload["message"]
        self._id = jsonPayload["_id"]
    
    def __str__(self): return self.message
