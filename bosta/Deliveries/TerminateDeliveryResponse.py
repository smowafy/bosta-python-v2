
class TerminateDeliveryResponse:

    def __init__(self, jsonResponse):
        self.message = self.fromJsonRespose(jsonResponse)
    
    def fromJsonRespose(self, jsonResponse): 
        return jsonResponse['message']

    def __str__(self):
        return self.message

