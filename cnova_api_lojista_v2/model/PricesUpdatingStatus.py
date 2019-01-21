#!/usr/bin/env python


class PricesUpdatingStatus:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'status': 'str',
            'processed_at': 'DateTime',
            'update_value': 'float',
            'site_name': 'str',
            'errors': 'list[Error]'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'status': 'status',
            'processed_at': 'processedAt',
            'update_value': 'updateValue',
            'site_name': 'siteName',
            'errors': 'errors'
            
        }

        
        #SKU do produto do lojista que deverá ser alterado
        
        self.sku_seller_id = None # str
        
        #Status do pedido
        
        self.status = None # str
        
        #Data do processamento
        
        self.processed_at = None # DateTime
        
        #Valor de atualização
        
        self.update_value = None # float
        
        #Nome do site
        
        self.site_name = None # str
        
        #Erros do pedido
        
        self.errors = None # list[Error]
        
