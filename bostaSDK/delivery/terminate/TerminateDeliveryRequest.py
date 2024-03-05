

class TerminateDeliveryRequest:
    def __init__(self, trackingNumber):
        """ Initialize new instance from TerminateDeliveryRequest class

        Parameters:
        trackingNumber (str): Tracking number

        Returns: New instance from TerminateDeliveryRequest class
        """
        self.trackingNumber = trackingNumber

    def get_trackingNumber(self):
        return self.trackingNumber

    def __str__(self): return self.trackingNumber
