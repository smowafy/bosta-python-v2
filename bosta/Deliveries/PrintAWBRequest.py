

class PrintAWBRequest:
    def __init__(self, deliveryIds=[]):
        self.ids = deliveryIds

    def toUrlQueryParamters(self):
        params = "&ids=" + self.ids if self.ids.len() is not 0 else ""
        return params