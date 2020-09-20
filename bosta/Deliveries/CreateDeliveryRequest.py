from bosta.utils.Address import Address
from bosta.utils.Receiver import Receiver
from bosta.utils.DeliverySpecs import DeliverySpecs


class CreateDeliveryRequest:

    def __init__(self, deliveryType, cod, dropOffAddress:Address, receiver: Receiver):
        """Create new delivery 

        Parameters:
        deliveryType (int)
        specs (DeliverySpecs)
        dropOffAddress (Address)
        cashOnDelivery (int): cash on delivert amount
        receiver (Receiver)

  
        Returns:
        object:Returning new delivery tracking number

        """
        self.type = deliveryType
        self.cod = cod
        self.dropOffAddress = dropOffAddress
        self.receiver = receiver

    def toJSONPayload(self): 
        return {
            "type": self.type,
            "cod": self.cod,
            "dropOffAddress": self.dropOffAddress,
            "receiver": self.receiver
        }


