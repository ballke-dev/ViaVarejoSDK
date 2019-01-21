#!/usr/bin/env python

import sys
import os

from ..model import *


class WarehousesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_warehouses(self, **kwargs):
        """Recupera uma lista de armazéns habilitados para um lojista
        <p>Recupera uma lista de armazéns habilitados para um lojista.</p>

        Args:
            

        Returns: GetWarehousesResponse
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_warehouses" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/warehouses'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetWarehousesResponse')
        return responseObject
        
        
        
    


