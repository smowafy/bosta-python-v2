
class BostaClient:
    def __init__(self, apiKey, apiBase):
        self.apiKey = apiKey
        self.apiBase = apiBase

    def get_apiKey(self): return self.apiKey
    def get_apiBase(self): return self.apiBase

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
