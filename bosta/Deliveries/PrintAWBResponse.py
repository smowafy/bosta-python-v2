
class PrintAWBResponse:
    def __init__(self, jsonResponse):
        self.data = self.fromJsonResponse(jsonResponse)

    def fromJsonResponse(self, jsonResponse):
        return jsonResponse["data"]

    def __str__(self): return self.data