

class PrintAWBRequest:
    def __init__(self, deliveryIds=[]):
        self.ids = deliveryIds

    def toUrlQueryParamters(self):
        params = {}
        if len(self.ids) is not 0: params["ids"] = self.ids
        return params