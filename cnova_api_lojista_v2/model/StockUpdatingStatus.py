#!/usr/bin/env python


class StockUpdatingStatus:

    def __init__(self):
        self.swaggerTypes = {
            'warehouse': 'int',
            'sku_seller_id': 'str',
            'status': 'str',
            'processed_at': 'DateTime',
            'update_value': 'float',
            'refer': 'str',
            'sku_site': 'str',
            'site_list': 'list[str]',
            'errors': 'list[Error]'
            
        }

        self.attributeMap = {
            'warehouse': 'warehouse',
            'sku_seller_id': 'skuSellerId',
            'status': 'status',
            'processed_at': 'processedAt',
            'update_value': 'updateValue',
            'refer': 'refer',
            'sku_site': 'skuSite',
            'site_list': 'siteList',
            'errors': 'errors'
            
        }

        
        #Localização fisica do estoque
        
        self.warehouse = None # int
        
        #SKU do produto do lojista que deverá ser alterado
        
        self.sku_seller_id = None # str
        
        #Status da solicitação de atualização
        
        self.status = None # str
        
        #Data do processamento
        
        self.processed_at = None # DateTime
        
        #Valor de atualização
        
        self.update_value = None # float
        
        #Arquivo de referência da atualização
        
        self.refer = None # str
        
        #SKU do site onde o estoque será atualizado
        
        self.sku_site = None # str
        
        
        self.site_list = None # list[str]
        
        #Erros do pedido
        
        self.errors = None # list[Error]
        
