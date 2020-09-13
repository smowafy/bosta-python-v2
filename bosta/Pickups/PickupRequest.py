import os
import requests
import json
import logging

with open(os.path.join(os.getcwd(),'bosta-python/bosta/config.json')) as configFile:
    config = json.load(configFile)

class PickupRequests:
    
    apiKey = os.getenv('BOSTA_API_KEY', '')
    
    @classmethod
    def getBusinessPickupRequests(cls, pageId=0):
        try:
            headers = {
                "Authorization": cls.apiKey
            }
            params = {
                "pageId": pageId 
            }
            response = requests.get(config['BOSTA_URL'] + "pickups", params= params, headers=headers)
            return response.json()
        except Exception as exp:
            raise exp
    
    @classmethod
    def createNewPickup(
        cls, scheduledDate, scheduledTimeSlot,
        contactPersonName, contactPersonPhone,
        contactPersonEmail, notes="",
        ):
        try:
            logging.info("Create New Pickup")
            payload = {
                "scheduledDate": scheduledDate,
                "scheduledTimeSlot": scheduledTimeSlot,
                "contactPerson": {
                    "name": contactPersonName,
                    "phone": contactPersonPhone,
                    "email": contactPersonEmail
                },
                "notes": notes,
            }
            headers = {
                "Authorization": cls.apiKey
            }
            response = requests.post(config['BOSTA_URL'] + "pickups", headers=headers, payload=payload)
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp

    @classmethod
    def editPickupRequest(
        cls, id, scheduledDate, scheduledTimeSlot,
        contactPersonName, contactPersonPhone,
        contactPersonEmail, notes="",
        ):
        try:
            logging.info("Edit Pickup Request")
            payload = {
                "scheduledDate": scheduledDate,
                "scheduledTimeSlot": scheduledTimeSlot,
                "contactPerson": {
                    "name": contactPersonName,
                    "phone": contactPersonPhone,
                    "email": contactPersonEmail
                },
                "notes": notes,
            }
            headers = {
                "Authorization": cls.apiKey
            }
            response = requests.put(
                config['BOSTA_URL'] + "pickups/" + id,
                headers=headers, payload=payload
            )
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp

    @classmethod
    def deletePickup(cls, id):
        try:
            logging.info("Delete Pickup Request")

            headers = {
                "Authorization": cls.apiKey
            }
            response = requests.delete(
                config['BOSTA_URL'] + "pickups/" + id,
                headers=headers
            )
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp
    
    @classmethod
    def getPickupRequestDetails(cls, id):
        try:
            logging.info("Get Pickup Request")

            headers = {
                "Authorization": cls.apiKey
            }
            response = requests.get(
                config['BOSTA_URL'] + "pickups/" + id,
                headers=headers
            )
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp



if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
