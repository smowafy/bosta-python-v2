

class ListAllPickupResponse:

    def __init__(self, jsonResponseObj):
        self.pickups = self.fromJsonPayload
    
    def fromJsonPayload(self, jsonObj):
        data = jsonObj.result.pickups
        return data