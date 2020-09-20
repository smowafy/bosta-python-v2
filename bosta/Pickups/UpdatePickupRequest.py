class UpdatePickupRequest:
    def __init__(self, _id, businessId, scheduledDate,
        scheduledTimeSlot, contactPerson, businessLocationId,
        warehouseId, noOfPackages, notes):

        self._id = _id    
        self.businessId = businessId
        self.scheduledDate = scheduledDate
        self.scheduledTimeSlot = scheduledTimeSlot
        self.businessLocationId = businessLocationId
        self.contactPerson = contactPerson
        self.noOfPackages = noOfPackages
        self.notes = notes

    def get_id(self):
        return self._id
    
    def toJSONPayload(self):

        return {
           "businessId":  self.businessId,
           "scheduledDate": self.scheduledDate,
           "scheduledTimeSlot": self.scheduledTimeSlot,
           "businessLocationId": self.businessLocationId,
           "contactPerson": self.contactPerson,
           "noOfPackages": self.noOfPackages,
           "notes": self.notes,
        }

