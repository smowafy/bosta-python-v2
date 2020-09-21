

class ListAllDeliveriesRequest:
    def __init__(self, pageNumber=None, limit=None):
        self.pageNumber = pageNumber
        self.limit = limit
    
    def toUrlQueryParamters(self):
        params = {}
        if self.pageNumber is not None: params["pageNumber"] = self.pageNumber
        if self.limit is not None: params["limit"] = self.limit
        return params