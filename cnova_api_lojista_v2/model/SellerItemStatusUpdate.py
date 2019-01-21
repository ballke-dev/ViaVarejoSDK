#!/usr/bin/env python


class SellerItemStatusUpdate:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'status': 'list[SellerItemStatus]'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'status': 'status'
            
        }

        
        #SKU do produto do lojista que deverá ser alterado
        
        self.sku_seller_id = None # str
        
        #Status do produto
        
        self.status = None # list[SellerItemStatus]
        
