

class GetPickupDetailsResponse:

    def __init__(self, jsonResponse):
        self.fromJSONPayload(jsonResponse)

    def fromJSONPayload(self, jsonResponse):
        pickup = jsonResponse["message"]
        self._id = pickup["_id"]
        self.puid = pickup["puid"]
        self.business = pickup["business"]
        self.scheduledDate = pickup["scheduledDate"]
        self.scheduledTimeSlot = pickup["scheduledTimeSlot"]
        self.contactPerson = pickup["contactPerson"]
        self.businessLocationId = pickup["businessLocationId"]
        self.deliveries = pickup["deliveries"]
        self.state = pickup["state"]
        self.createdAt = pickup["createdAt"]
        self.tickets = pickup["tickets"]

    def __str__(self):
        return self._id
