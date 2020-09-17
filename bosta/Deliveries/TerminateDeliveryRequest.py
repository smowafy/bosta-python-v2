

class TerminateDeliveryRequest:
    def __init__(self, deliveryId):
        self._id = deliveryId
    
    def get_deliveryId(self):
        return self._id