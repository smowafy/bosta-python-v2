class City:
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def listAll(self):
        """ List all citites

        Returns: List of available cities
        """
        try:
            headers = {
                "accept": "application/json"
            } 
            response = self.apiClient.send(
                'get',
                "api/v0/cities",
                headers
            )
            return response.json()
        except Exception as exp:
            raise exp