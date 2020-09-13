
import logging
import requests

class CreatePickupRequest:

    def __init__(self, businessId, scheduledDate,
        scheduledTimeSlot, contactPerson, businessLocationId,
        warehouseId, noOfPackages, notes):
        
        self.businessId = businessId
        self.scheduledDate = scheduledDate
        self.scheduledTimeSlot = scheduledTimeSlot
        self.businessLocationId = businessLocationId
        self.contactPerson = contactPerson
        self.noOfPackages = noOfPackages
        self.notes = notes
    
    def toJsonPayload(self):
        return {
           "businessId":  self.businessId,
           "scheduledDate": self.scheduledDate,
           "scheduledTimeSlot": self.scheduledTimeSlot,
           "businessLocationId": self.businessLocationId,
           "contactPerson": self.contactPerson,
           "noOfPackages": self.noOfPackages,
           "notes": self.notes,
        }




