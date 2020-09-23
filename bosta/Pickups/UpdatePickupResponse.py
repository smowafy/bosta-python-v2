

class UpdatePickupResponse:
    def __init__(self, jsonResponse):
        self.message = self.fromJSONResponse(jsonResponse)

    def fromJSONResponse(self, jsonResponse):
        return jsonResponse["message"]
    
    def __str__(self): 
        return self.message

    
