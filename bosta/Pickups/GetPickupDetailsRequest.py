

class GetPickupDetailsRequest:
    def __init__(self, pickupId):
        self._id = pickupId

    def get_pickupId(self):
        return self._id

    def __str__(self):
        return str(self._id)
