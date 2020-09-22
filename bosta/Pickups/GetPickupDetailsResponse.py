

class GetPickupDetailsResponse:

    def __init__(self, jsonResponse={}):
        self.fromJSONPayload(jsonResponse)

    def fromJSONPayload(self, jsonResponse):
        self._id = jsonResponse["_id"]
        self.puid = jsonResponse["puid"]
        self.business = jsonResponse["business"]
        self.scheduledDate = jsonResponse["scheduledDate"]
        self.scheduledTimeSlot = jsonResponse["scheduledTimeSlot"]
        self.contactPerson = jsonResponse["contactPerson"]
        self.businessLocationId = jsonResponse["businessLocationId"]
        self.deliveries = jsonResponse["deliveries"]
        self.state = jsonResponse["state"]
        self.createdAt = jsonResponse["createdAt"]
        self.tickets = jsonResponse["tickets"]
