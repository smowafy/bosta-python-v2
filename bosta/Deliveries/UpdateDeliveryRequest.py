from ..utils import Receiver, Address
class UpdateDeliveryRequest:

    def __init__(
        self, deliveryId: int ,receiver: Receiver, 
        pickUpAddress: Address, dropOffAddress: Address,
        returnAddress: Address,notes: str, 
        businessReference:str,
        webhookUrl: str, cod: int
        ):
        self._id = deliveryId
        self.receiver = receiver
        self.pickUpAddress = pickUpAddress
        self.dropOffAddress = dropOffAddress
        self.returnAddress = returnAddress
        self.notes = notes
        self.businessReference = businessReference
        self.webhookUrl = webhookUrl
        self.cod = cod

    def get_deliveryId(self): 
        return self._id

    def toJsonPayload(self):
        payload = {}
        if self.receiver is not None:
            payload['receiver'] = self.receiver
        if self.pickUpAddress is not None:
            payload['pickUpAddress'] = self.pickUpAddress
        if self.dropOffAddress is not None:
            payload['dropOffAddress'] = self.dropOffAddress
        if self.returnAddress is not None:
            payload['returnAddress'] = self.returnAddress
        if self.notes is not None:
            payload['notes'] = self.notes
        if self.businessReference is not None:
            payload['businessReference'] = self.businessReference
        if self.webhookUrl is not None:
            payload['webhookUrl'] = self.webhookUrl
        if self.cod is not None:
            payload['cod'] = self.cod    
        return payload


   