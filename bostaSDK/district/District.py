class District:
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def listAll(self):
        """ List all districts

        Returns: List of available districts
        """
        try:
            headers = {
                "accept": "application/json"
            }
            response = self.apiClient.send(
                'get',
                "/cities/getAllDistricts",
                headers
            )
            if (response.status_code != 200):
                return response.text
            return response.json()
        except Exception as exp:
            raise exp

    def listForCity(self, cityId):
        """ List all districts for a city

        Parameters:
        cityId (int)

        Returns: List of available districts for a city
        """
        try:
            headers = {
                "accept": "application/json"
            }
            response = self.apiClient.send(
                'get',
                "/cities/{}/districts".format(cityId),
                headers
            )
            if (response.status_code != 200):
                return response.text
            return response.json()
        except Exception as exp:
            raise exp
