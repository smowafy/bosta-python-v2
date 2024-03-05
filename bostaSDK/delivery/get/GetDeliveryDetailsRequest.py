

class GetDeliveryDetailsRequest:
    def __init__(self, trackingNumber):
        """ Initialize new instance from GetDeliveryDetailsRequest class

        Parameters:
        trackingNumber (str): Tracking Number

        Returns: New instance from GetDeliveryDetailsRequest class
        """
        self.trackingNumber = trackingNumber

    def __str__(self):
        return str(self.trackingNumber)

    def get_trackingNumber(self):
        return self.trackingNumber
