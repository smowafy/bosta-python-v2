import os

from bosta.apiClient import ApiClient
from bosta.delivery import list, create, update, track, printAWB, get
from bosta.utils import Receiver, Address, ContactPerson

apiKey = os.getenv("BOSTA-API-KEY")
baseUrl = os.getenv("BOSTA-BASE-URL")

apiClient = ApiClient(apiKey, baseUrl)
deliveryTypes = apiClient.deliveyTypes

#List Deliveries 
apiClient.delivery.listAll(list.ListAllDeliveriesRequest(3,10))

#Create new delivery
reciever = Receiver("sohila", "Boghdady", "sohila_bogdady@hotmail.com", "01093155077")
dropOffAddress = Address("EG-01", "Maadi", "Maadi", "104")
createDeliveryReq = create.CreateDeliveryRequest(
    deliveryTypes['SEND']['code'], 100, dropOffAddress, reciever 
)
deliveryId = apiClient.delivery.create(createDeliveryReq)

#Print Airway Bill
apiClient.delivery.printAirWayBill(printAWB.PrintAWBRequest([deliveryId]))

#Track Delivery
apiClient.delivery.track(track.TrackDeliveryRequest(deliveryId))

#Get Delivery
apiClient.delivery.get(get.GetDeliveryDetailsRequest(deliveryId))