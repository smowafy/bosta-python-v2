

class TrackDeliveryRequest:
    def __init__(self, deliveryId):
        self._id = deliveryId
    
    def __str__(self):
        return self._id
    
    def get_deliveryId(self):
        return self._id

