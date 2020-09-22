

class ListAllPickupResponse:

    def __init__(self, jsonResponseObj):
        self.pickups = self.fromJSONPayload
    
    def fromJSONPayload(self, jsonObj):
        data = jsonObj.result.pickups
        return data