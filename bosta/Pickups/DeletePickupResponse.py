

class DeletePickupResonse:
    def __init__(self, jsonResponse):
        self.message = self.fromJsonResponse(jsonResponse)
    
    def fromJsonResponse(self, jsonResponse):
        return jsonResponse["message"]
    
    def __str__(self):
        self.message

    
