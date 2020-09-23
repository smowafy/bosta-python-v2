

class TrackDeliveryResponse:

    def __init__(self, jsonResponse):
        self._id, self.trackingNumber, self.state_history = self.fromJSONResponse(jsonResponse)

    def fromJSONResponse(self, jsonResponse):
        state_history = []
        for obj in jsonResponse["state-history"]:
            state_history.append({
                "state": obj["state"],
                "time": obj["timestamp"],
                "takenBy": obj["takenBy"]["userName"]
            })
        return jsonResponse["_id"], jsonResponse["trackingNumber"], state_history
    
    def __str__(self):
        str(self._id)