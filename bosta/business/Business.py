import os
import requests
import json
import logging

from bosta.ApiClient.ApiClient import BostaClient


class BusinessInfo:
    def __init__(self):
        self.apiClient = BostaClient(
            os.environ.get('BOSTA_API_KEY'),
            os.environ.get('BOSTA_API_BASE')
        )
    
    def getBusinessSubAccount(self, pageId=0):
        try:
            logging.info('Get Business Sub Account')
            url  = self.apiClient.get_apiBase() + "businessSubAccount"
            headers = {
                "Authorization": self.apiClient.get_apiKey()
            }
            params = {
                "pageId": pageId 
            }
            response = requests.get(url, params= params, headers=headers)
            if (response.status_code != 200): return response.text
            return response.json()
        except Exception as exp:
            logging.error(exp)
            raise exp
