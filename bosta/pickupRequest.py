import os
import requests
import json
import logging

with open('config.json') as configFile:
    config = json.load(configFile)

class PickupRequests:
    def __init__(self):
        self.apiKey = os.getenv('BOSTA_API_KEY', '')

    def getBusinessPickupRequests(self, pageId=0):
        try:
            headers = {
                "Authorization": self.apiKey
            }
            params = {
                "pageId": pageId 
            }
            response = requests.get(config['BOSTA_URL'] + "pickups", params= params, headers=headers)
            return response.json()
        except Exception as exp:
            raise exp
    
    def createNewPickup(
        self, scheduledDate, scheduledTimeSlot,
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
                "Authorization": self.apiKey
            }
            response = requests.post(config['BOSTA_URL'] + "pickups", headers=headers, payload=payload)
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
