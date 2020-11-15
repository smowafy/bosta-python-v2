

class ListAllPickupResponse:
    def __init__(self, jsonResponseObj):
        """ Initialize new instance from ListAllPickupResponse class

        Parameters:
        jsonPayload (dict): JSON response object

        Returns: instance from ListAllPickupResponse

        """
        self.fromJSONPayload(jsonResponseObj)

    def fromJSONPayload(self, jsonResponseObj):
        """
        Extract pickups from json response object

        Parameters:
        jsonResponse (dict): JSON response object

        """
        if jsonResponseObj.get("data"):
            self.pickups = jsonResponseObj["data"]["pickups"]
            self.message = jsonResponseObj["message"]
            self.success = jsonResponseObj["success"]
        else:
            self.pickups = []
            self.message = str(jsonResponseObj)

    def __str__(self):
        return self.message
    
    def get_pickups(self):
        return self.pickups

    def get_message(self):
        return self.message
