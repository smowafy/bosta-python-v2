

class DeletePickupResonse:
    def __init__(self, jsonResponse):
        """
        Initialize new instance from DeletePickupResonse class

        Parameters:
        jsonResponse (dict): JSON response object

        Returns:
        instance from DeletePickupResonse

        """
        self.fromJsonResponse(jsonResponse)

    def fromJsonResponse(self, jsonResponse):
        """
        Extract message field from json response object

        Parameters:
        jsonResponse (dict): JSON response object
        """
        if jsonResponse.get("message") is not None:
            self.message = jsonResponse["message"]
        else:
            self.message = str(jsonResponse )

    def __str__(self):
        self.message
