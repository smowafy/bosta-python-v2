# Bosta Python SDK

This repository contains the open source Python SDK for integrating Bosta's APIs into your Python application.

# Table of Contents

- [APIs Documentation](# apis-documentation)
- [Installation](#installation)
- [Usages](#usages)
- [Contribution](#contribution)
- [License](#license)

# APIs Documentation

- [Staging](https://stg-app.bosta.co/docs) APIs swagger documentation.
- [Production](https://app.bosta.co/docs) APIs swagger documentation.

# Installation

You can install the package via [pip](https://pypi.org/project/pip/). Run the following command:

```bash
pip install bostaSDK
```

# Usage

    ``` python
    import os

    from bostaSDK.apiClient import ApiClient
    from bostaSDK.delivery import list, create, update, track, printAWB, get, terminate
    from bostaSDK.pickup import create, list, get, update, delete
    from bostaSDK.utils import Receiver, Address, ContactPerson


    apiKey=os.environ["BOSTA-API-KEY"]="your api key"
    baseUrl=os.environ["BOSTA-BASE-URL"]="bosta base url"

    apiClient=ApiClient(apiKey, baseUrl)

    ################ Deliveries ################# 
    ################# List Deliveries ################# 
    # 1. Create new instance from ListAllDeliveriesRequest
    #  Parameters:
    #     pageNumber (int): Page Number
    #     limit (int): Number of deliveries returned from api
    listAllDeliveriesRequest = list.ListAllDeliveriesRequest(3, 10) 
    
    # 2. Send list all deliveries request
    #   Parameters:
    #       listAllDeliveriesRequest (ListAllDeliveriesRequest)
    apiClient.delivery.listAll(listAllDeliveriesRequest)


    ################# Create new Delivery #################    
    # 1. Create new Receiver  
    # Parameters:
    #   firstName (str)
    #   lastName (str)
    #   email (str)
    #   phone (str)
    reciever=Receiver(
    "firstName",
    "lastName",
    "test@example.com",
     "01090055000"
    )

    # 2. Create new Address  
    #   Parameters:
    #       cityCode (str)
    #       zone (str)
    #       secondLine (str)
    #       district (str)
    #       buildingNumber (int)
    #       floor (int)
    #        apartment (int)
    dropOffAddress=Address("EG-01", "Maadi", "Maadi", "104")

    # 3. Create new instance from CreateDeliveryRequest
    #    Parameters:
    #       deliveryType (int)
    #       specs (DeliverySpecs)
    #       dropOffAddress (Address)
    #       cashOnDelivery (int): Cash on delivery amount
    #       receiver (Receiver)
    createDeliveryReq=create.CreateDeliveryRequest(
        deliveryTypes['SEND']['code'], 100, dropOffAddress, reciever
    )

    # 4. Send Create Delivery Request
    #   Parameters:
    #       createDeliveryReq (CreateDeliveryRequest)

    deliveryId=apiClient.delivery.create(createDeliveryReq)


    ################# Print Airway Bill ################# 
    # 1. Create new instance from PrintAWBRequest
    #   Parameters:
    #       deliveryIds (array): List of delivery ids
    printAWBreq = printAWB.PrintAWBRequest([deliveryId])

    # 2. Send Print Airway bill request
    #   Parameters:
    #       printAWBreq (PrintAWBRequestrray)
    apiClient.delivery.printAirWayBill(printAWBreq)


    ################# Track Delivery #################
    # 1. Create new instance from TrackDeliveryRequest
    #   Parameters:
    #       deliveryId (str)
    trackDeliveryRequest = track.TrackDeliveryRequest(deliveryId)

    # 2. Send track delivery request
    #   Parameters:
    #       trackDeliveryRequest (TrackDeliveryRequest)
    apiClient.delivery.track(trackDeliveryRequest)


    ################# Get Delivery #################
    # 1. Create new instance from GetDeliveryDetailsRequest
    #   Parameters:
    #       deliveryId (str)
    getDeliveryDetailsRequest = get.GetDeliveryDetailsRequest(deliveryId)
    
    # 2. Send get delivery request
    #   Parameters:
    #       getDeliveryDetailsRequest (GetDeliveryDetailsRequest)
    apiClient.delivery.get(getDeliveryDetailsRequest)


    ################# Update Delivery #################
    # 1. Create new instance from UpdateDeliveryRequest
    #    Parameters:
    #       deliveryId (str): Delivery Id
    #       specs (DeliverySpecs)
    #       pickUpAddress (Address, optinal)
    #       dropOffAddress (Address, optinal)
    #       returnAddress (Address, optinal)
    #       cod (int, optinal): Cash on delivery amount
    #       receiver (Receiver, optinal)
    #       businessReference (str, optinal): Business refrence
    #       webhookUrl (str, optinal)
    newReciever=Receiver("user", "test", "test@example.com", "01090055000")
    updateDeliveryRequest = update.UpdateDeliveryRequest(
        deliveryId,
        receiver=newReciever,
         cod=120
    )
    # 2. Send update delivery request
    #   Parameters:
    #       updateDeliveryRequest (UpdateDeliveryRequest)
    apiClient.delivery.update(updateDeliveryRequest)
    
    
    #################  Terminate Delivery #################
    # 1. Create new instance from TerminateDeliveryRequest
    #   Parameters:
    #       deliveryId (str)
    terminateDeliveryRequest = terminate.TerminateDeliveryRequest(deliveryId)

    # 2. Send terminate delivery request
    #   Parameters:
    #       terminateDeliveryRequest (TerminateDeliveryRequest)
    apiClient.delivery.terminate(terminateDeliveryRequest)


    ################ Pickups ################# 
    ################ Create New Pickup #################
    # 1. Create new instance from ContactPerson
    #   Parameters:
    #       name (str)
    #       phone (str)
    #       email (str)
    contactPerson = ContactPerson("userName", "01090000000", "example@bosta.co")

    # 2. Create new instance from CreatePickupRequest
    #   Parameters:
    #       scheduledDate (str): Pickup scheduled date
    #       scheduledTimeSlot (str): "10:00 to 13:00" or "13:00 to 16:00"
    #       contactPerson (ContactPerson)
    #       businessId (str)
    #       businessLocationId (str)
    #       warehouseId (str)
    #       noOfPackages (int)
    #       notes (str) 
    createPickupRequest = create.CreatePickupRequest(
        "Mon Nov 7 2021 00:00:00 GMT+0200",
        apiClient.pickupTimeSlots[0], contactPerson
    )
    # 3. Send create pickup request
    #   Parameters:
    #       createPickupRequest (CreatePickupRequest)
    newPickupId=apiClient.pickup.create(createPickupRequest)


    ################ List Pickups #################
    # 1. Create new instance from ListAllPickupsRequest
    #   Parameters:
    #     pageId (int)
    #     sortBy (str)
    #     sortValue (str)
    listAllPickupsRequest = list.ListAllPickupsRequest(2)

    # 2. Send list all pickups request
    #   Parameters:
    #       listAllPickupsRequest (ListAllPickupsRequest)
    apiClient.pickup.listAll(listAllPickupsRequest)


    ################ Get Pickup #################
    # 1. Create new instance from GetPickupDetailsRequest
    #   Parameters:
    #     pickupId (str): Pickup Id
    getPickupDetailsRequest = get.GetPickupDetailsRequest(newPickupId)
    
    # 2. Send get pickup request
    #   Parameters:
    #       getPickupDetailsRequest (GetPickupDetailsRequest)
    apiClient.pickup.get(getPickupDetailsRequest)


    ################ Update Pickup #################
    # 1. Create new instance from UpdatePickupRequest
    #   Parameters:
    #     _id (str): Pickup Id
    #     businessId (str)
    #     scheduledDate (str)
    #     scheduledTimeSlot (str)
    #     contactPerson (ContactPerson)
    #     businessLocationId (str)
    #     warehouseId (str)
    #     noOfPackages (str)
    #     notes (str)

    updatePickupRequest = update.UpdatePickupRequest(
        newPickupId, 
        contactPerson=ContactPerson("newUser", "010193155922", "user2@bosta.co")
    )
      
    # 2. Send update pickup request
    #   Parameters:
    #       updatePickupRequest (UpdatePickupRequest)
    apiClient.pickup.update(updatePickupRequest)

    
    ################ Delete Pickup #################
    # 1. Create new instance from DeletePickupRequest
    #   Parameters:
    #     pickupId (str): Pickup Id
    deletePickupRequest = delete.DeletePickupRequest(newPickupId)

    # 2. Send delete pickup request
    #   Parameters:
    #       deletePickupRequest (UpdatePickupRequest)
    apiClient.pickup.delete(DeletePickupRequest)

    ```

## Contribution

We are open to, and grateful for, any contributions made by the community.
By contributing to Bosta, you agree to abide by the code of conduct.
- [Contributing Guide](CONTRIBUTING.md) 
- [Code of Conduct](CODE_OF_CONDUCT.md)

## License

The MIT License (MIT) [License](LICENSE).
