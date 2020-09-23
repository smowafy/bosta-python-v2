

class ListAllPickupResponse:
    def __init__(self, jsonResponseObj):
        self.pickups = self.fromJSONPayload(jsonResponseObj)
    
    def fromJSONPayload(self, jsonResponseObj):
        return jsonResponseObj["result"]["pickups"]

    def __str__(self):
        return str(self.pickups)