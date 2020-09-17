import json

class TerminateDeliveryResponse:

    def __init__(self, jsonResponse):
        self.message = self.fromJsonRespose(jsonResponse)
    
    def fromJsonRespose(self, jsonResponse):
        data = json.loads(jsonResponse)
        return data.message

