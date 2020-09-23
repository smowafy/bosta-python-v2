

class ListAllPickupsRequest:

    def __init__(self, pageId, sortBy=None, sortValue= None):
        self.pageId = pageId
        self.sortBy = sortBy
        self.sortValue = sortValue

    def toQueryParamters(self):
        params = {
            "pageId": self.pageId,
        }
        if self.sortBy is not None: params["sortBy"] = self.sortBy
        if self.sortValue is not None: params["sortValue"] = self.sortValue
        return params
