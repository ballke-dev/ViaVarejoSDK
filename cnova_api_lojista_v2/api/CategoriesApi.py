#!/usr/bin/env python

import sys
import os

from ..model import *


class CategoriesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_categories(self, **kwargs):
        """Recupera uma lista de categorias
        <p>Recupera uma lista de categorias existentes no Marketplace.</p><p class='obs obs-danger'>Por padrão, o acesso a este serviço está bloqueado e só será liberado para quem irá realizar desduplicação de produtos.<br/>Para mais informações, entre com seu login e senha e abra um Chamado para nossa equipe de suporte.</p>

        Args:
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetCategoriesResponse
        """

        allParams = ['_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_categories" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/categories'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetCategoriesResponse')
        return responseObject
        
        
        
    
    def get_category_by_id(self, **kwargs):
        """Recupera detalhes de uma categoria informada
        <p>Recupera detalhes da categoria informada.</p><p class='obs obs-danger'>Por padrão, o acesso a este serviço está bloqueado e só será liberado para quem irá realizar desduplicação de produtos.<br/>Para mais informações, entre com seu login e senha e abra um Chamado para nossa equipe de suporte.</p>

        Args:
            level_id, str: Id da categoria. (required)
            

        Returns: Category
        """

        allParams = ['level_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_category_by_id" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/categories/{levelId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('level_id' in params):
            replacement = str(self.apiClient.toPathValue(params['level_id']))
            resourcePath = resourcePath.replace('{' + 'levelId' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Category')
        return responseObject
        
        
        
    


