#!/usr/bin/env python


class Error:

    def __init__(self):
        self.swaggerTypes = {
            'code': 'str',
            'http_status': 'str',
            'type': 'str',
            'message': 'str',
            'sku_seller_id': 'str'
            
        }

        self.attributeMap = {
            'code': 'code',
            'http_status': 'httpStatus',
            'type': 'type',
            'message': 'message',
            'sku_seller_id': 'skuSellerId'
            
        }

        
        #Código de retorno da aplicação
        
        self.code = None # str
        
        #Código de retorno do protocólo HTTP
        
        self.http_status = None # str
        
        #Tipo do erro
        
        self.type = None # str
        
        #Descrição do erro
        
        self.message = None # str
        
        #Identificador do seller item que originou o problema
        
        self.sku_seller_id = None # str
        
