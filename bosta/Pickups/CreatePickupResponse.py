

class CreatePickupResponse:
 
    def __init__(self, jsonResponseObj):
        self.fromJsonPayload(jsonResponseObj)

    def fromJsonPayload(self, responseObj):
        self._id = responseObj["_id"]
        self.puid = responseObj["puid"]
        self.businessId = responseObj["businessId"]
        self.businessLocationId = responseObj["businessLocationId"]
        self.scheduledDate = responseObj["scheduledDate"]
        self.scheduledTimeSlot = responseObj["scheduledTimeSlot"]
        self.contactPerson = responseObj["contactPerson"]
        self.createdAt = responseObj["createdAt"]
        self.updatedAt = responseObj["updatedAt"]
        
