import os
import requests
import json
import logging

with open('config.json') as configFile:
    config = json.load(configFile)

class BusinessInfo:
    def __init__(self):
        self.apiKey = os.getenv('BOSTA_API_KEY', '')

    def getBusinessSubAccount(self, pageId=0):
        try:
            logging.info('Get Business Sub Account')
            headers = {
                "Authorization": self.apiKey
            }
            params = {
                "pageId": pageId 
            }
            response = requests.get(config['BOSTA_URL'] + "businessSubAccount", params= params, headers=headers)
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
