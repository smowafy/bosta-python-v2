

class DeletePickupResonse:
    def __init__(self, response):
        self.statusCode = response.status_code
        self.message = response.json().message

    
