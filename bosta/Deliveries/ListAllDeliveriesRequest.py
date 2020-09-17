

class ListAllDeliveriesRequest:
    def __init__(self, pageNumber=None, limit=None):
        self.pageNumber = pageNumber
        self.limit = limit
    
    def toUrlQueryParamters(self):
        params = "&pageNumber=" + self.pageNumber if self.pageNumber is not None else ""
        params += "&limit=" + self.limit if self.limit is not None else ""
        return params