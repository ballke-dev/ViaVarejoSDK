#!/usr/bin/env python


class ProductResponseItem:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller': 'SellerItemReference',
            'status': 'str',
            'created_at': 'DateTime'
            
        }

        self.attributeMap = {
            'sku_seller': 'skuSeller',
            'status': 'status',
            'created_at': 'createdAt'
            
        }

        
        #SKU do produto do Lojista
        
        self.sku_seller = None # SellerItemReference
        
        #Status do produto
        
        self.status = None # str
        
        #Data de envio do produto
        
        self.created_at = None # DateTime
        
