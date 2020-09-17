
import json
class PrintAWBResponse:
    def __init__(self, jsonResponse):
        self.data = self.fromJsonResponse(jsonResponse)

    def fromJsonResponse(self, jsonResponse):
        return json.loads(jsonResponse)["data"]