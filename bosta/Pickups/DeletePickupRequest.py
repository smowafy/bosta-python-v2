
class DeletePickupRequest:
    def __init__(self, pickupId):
        self._id = pickupId

    def get_pickupId(self): 
        return self._id