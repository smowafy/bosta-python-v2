from bosta.apiClient import ApiClient
from bosta.utils import ContactPerson
from bosta.pickup import create, list, get, update, delete

apiClient = ApiClient("<business-api-key>", "<bosta-base-url>")

# Create New Pickup
newPickupId = apiClient.pickup.create(
    create.CreatePickupRequest(
     "Mon Nov 7 2020 00:00:00 GMT+0200", apiClient.pickupTimeSlots[0],
      ContactPerson ("m", "010193155997", "example@bosta.co")
    )
)

#List Pickups 
apiClient.pickup.listAll(list.ListAllPickupsRequest(2))

#Get Pickup 
apiClient.pickup.get(
    get.GetPickupDetailsRequest(newPickupId)
)

#Update Pickup 
apiClient.pickup.update(update.UpdatePickupRequest(
    newPickupId, contactPerson=ContactPerson ("user", "010193155922", "user@bosta.co")
))