

class ListAllPickupsRequest:

    def __init__(self, pageId, sortBy=None, sortValue= None):
        self.pageId = pageId
        self.sortBy = sortBy
        self.sortValue = sortValue

    def toQueryParamters(self):
        params = "?pageId=" + self.pageId 
        params += "&sortBy=" + self.sortBy if self.sortBy is not None else ""
        params += "&sortBy=" + self.sortBy if self.sortBy is not None else ""
        return params
