#!/usr/bin/env python

import sys
import os

from ..model import *


class SitesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_sites(self, **kwargs):
        """Recupera uma lista de sites
        <p>Recupera uma lista de sites que operam como Marketplace.</p>

        Args:
            

        Returns: GetSitesResponse
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_sites" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/sites'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSitesResponse')
        return responseObject
        
        
        
    


