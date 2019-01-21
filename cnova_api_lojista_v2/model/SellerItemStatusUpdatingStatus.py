#!/usr/bin/env python


class SellerItemStatusUpdatingStatus:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'site': 'str',
            'status': 'str',
            'processed_at': 'DateTime',
            'update_value': 'str',
            'site_name': 'str',
            'sku_site': 'str',
            'errors': 'list[Error]'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'site': 'site',
            'status': 'status',
            'processed_at': 'processedAt',
            'update_value': 'updateValue',
            'site_name': 'siteName',
            'sku_site': 'skuSite',
            'errors': 'errors'
            
        }

        
        #SKU do produto do lojista que deverá ser alterado
        
        self.sku_seller_id = None # str
        
        #Site de venda
        
        self.site = None # str
        
        #Status do produto
        
        self.status = None # str
        
        #Data do processamento
        
        self.processed_at = None # DateTime
        
        #Atualização
        
        self.update_value = None # str
        
        #Nome do site
        
        self.site_name = None # str
        
        #Sku do site
        
        self.sku_site = None # str
        
        #Lista de erros que ocorreram produto
        
        self.errors = None # list[Error]
        
