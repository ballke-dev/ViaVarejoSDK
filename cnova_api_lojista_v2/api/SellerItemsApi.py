#!/usr/bin/env python

import sys
import os

from ..model import *


class SellerItemsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_seller_items(self, **kwargs):
        """Recupera todos os produtos que estão associados ao Lojista
        Recupera todos os produtos que estão associados ao Lojista, mesmo os que não estão disponíveis para venda.

        Args:
            site, str: Site do qual deseja consultar o produto. Se o parâmetro não for informado, serão trazidos apenas produtos do Extra. Consulte a lista completa de sites disponíveis no serviço <a href='#!/sites' target='_blank'><strong>GET /sites</strong></a> (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetSellerItemsResponse
        """

        allParams = ['site', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_seller_items" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/sellerItems'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('site' in params):
            queryParams['site'] = self.apiClient.toPathValue(params['site'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSellerItemsResponse')
        return responseObject
        
        
        
    
    def get_seller_items_by_status_active(self, **kwargs):
        """Recupera produtos do Lojista que estão disponíveis para venda
        Recupera apenas os produtos do Lojista que estão disponíveis para venda, ou seja, que possuem estoque e preço atualizados e imagem(ns) válida(s).

        Args:
            site, str: Site do qual deseja consultar os produtos. Se o parâmetro não for informado, serão trazidos apenas produtos do Extra. Os possíveis sites são: 'EX', 'PF', 'CB', 'EH', 'BT', 'CD'. Consulte a lista completa de sites disponíveis no serviço <a href='#!/sites' target='_blank'><strong>GET /sites</strong></a> (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta (required)
            

        Returns: GetSellerItemsResponse
        """

        allParams = ['site', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_seller_items_by_status_active" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/sellerItems/status/selling'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('site' in params):
            queryParams['site'] = self.apiClient.toPathValue(params['site'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSellerItemsResponse')
        return responseObject
        
        
        
    
    def get_seller_item_by_sku_seller_id(self, **kwargs):
        """Recupera detalhes do item do Lojista através do skuSellerId (sku do produto do Lojista) informado
        Recupera detalhes do item do Lojista através do skuSellerId (sku do produto do Lojista) informado.

        Args:
            sku_seller_id, str: SKU ID do Lojista. (required)
            site, str: Site do qual deseja consultar o produto. Se o parâmetro não for informado, serão trazidos apenas produtos do Extra. Consulte a lista completa de sites disponíveis no serviço <a href='#!/sites' target='_blank'><strong>GET /sites</strong></a> (required)
            

        Returns: SellerItem
        """

        allParams = ['sku_seller_id', 'site']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_seller_item_by_sku_seller_id" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/sellerItems/{skuSellerId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('site' in params):
            queryParams['site'] = self.apiClient.toPathValue(params['site'])
        

        

        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SellerItem')
        return responseObject
        
        
        
    
    def put_seller_item_prices(self, **kwargs):
        """Atualização de preço do item do Lojista
        <p>Atualiza o preço 'de' e o preço 'por' (preço real para venda) do item do Lojista informado.</p><p class='obs obs-danger'><strong>Atenção:</strong> <br/>Para proteção do lojista, existe uma regra de validação de preços que impede alterações muito grandes em uma única operação. Não é permitido a alteração com valores 50% menores que o valor atual. <br/>Para este tipo de crítica será retornado um Status HTTP <a href='../apis/index.html#error_codes'><strong>422</strong></a>, seguido da mensagem: <strong>Alteração não permitida, variação de preço muito grande.</strong></p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            sku_seller_id, str: SKU ID do Lojista. (required)
            body, Prices: Parâmetros para atualização de preço do SKU (required)
            

        Returns: str
        """

        allParams = ['sku_seller_id', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_seller_item_prices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/sellerItems/{skuSellerId}/prices'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def put_seller_item_status(self, **kwargs):
        """Ativação/Desativação de produto no Marketplace
        Atualiza o status do produto no Marketplace. Se setado para false, o produto é desativado e deixa de ser vendido no Marketplace.<p ='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            sku_seller_id, str: SKU ID do Lojista. (required)
            body, SellerItemStatus: Parâmetros para ativação/desativação do SKU. (required)
            

        Returns: str
        """

        allParams = ['sku_seller_id', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_seller_item_status" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/sellerItems/{skuSellerId}/status'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def put_seller_item_stock(self, **kwargs):
        """Atualização de estoque do item do Lojista
        <p>Atualiza a quantidade disponível para venda do Item do Lojista informado.</p><p class='obs'>Se atualizado para zero, o item não estará mais disponível para venda.</p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            sku_seller_id, str: SKU ID do Lojista. (required)
            body, Stock: Parâmetros para atualização de estoque do SKU (required)
            

        Returns: str
        """

        allParams = ['sku_seller_id', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_seller_item_stock" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/sellerItems/{skuSellerId}/stock'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    


