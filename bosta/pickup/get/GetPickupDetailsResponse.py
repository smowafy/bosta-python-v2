

class GetPickupDetailsResponse:

    def __init__(self, jsonResponse):
        """ 
        Initialize new instance from GetPickupDetailsResponse class

        Parameters: 
        jsonResponse (dict): JSON response object 
        
        Returns: 
        instance from GetPickupDetailsResponse

        """  
        self.fromJSONPayload(jsonResponse)

    def fromJSONPayload(self, jsonResponse):
        """ 
        Extract _id, pickupAddress, dropOffAddress,
        cod, receiver, state, type, creationTimestamp,
        trackingNumber, holder, timeline,
        and history fields from json response object

        Parameters: 
        jsonResponse (dict): JSON response object 
        """ 
        self._id = jsonResponse["_id"]
        self.pickupAddress = jsonResponse["pickupAddress"]
        self.dropOffAddress = jsonResponse["dropOffAddress"]
        self.cod = jsonResponse["cod"]
        self.receiver = jsonResponse["receiver"]
        self.state = jsonResponse["state"]
        self.type = jsonResponse["type"]
        self.trackingNumber = jsonResponse["trackingNumber"]
        self.holder = jsonResponse["holder"]
        self.timeline = jsonResponse["timeline"]
        self.history = jsonResponse["history"]
        self.creationTimestamp = jsonResponse["creationTimestamp"]

    def __str__(self):
        return self._id
