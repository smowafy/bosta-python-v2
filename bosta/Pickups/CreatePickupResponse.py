

class CreatePickupResponse:
 
    def __init__(self, jsonResponseObj):
        self.fromJSONPayload(jsonResponseObj)

    def fromJSONPayload(self, responseObj):
        newPickup = responseObj["message"]
        self._id = newPickup["_id"]
        self.puid = newPickup["puid"]
        self.business = newPickup["business"]
        self.businessLocationId = newPickup["businessLocationId"]
        self.scheduledDate = newPickup["scheduledDate"]
        self.scheduledTimeSlot = newPickup["scheduledTimeSlot"]
        self.contactPerson = newPickup["contactPerson"]
        self.createdAt = newPickup["createdAt"]
        self.updatedAt = newPickup["updatedAt"]
    
    def __str__(self):
        return self._id



        
