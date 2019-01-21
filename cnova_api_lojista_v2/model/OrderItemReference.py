#!/usr/bin/env python


class OrderItemReference:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'quantity': 'int'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'quantity': 'quantity'
            
        }

        
        #SKU do produto do lojista que deverá ser alterado
        
        self.sku_seller_id = None # str
        
        #Quantidade do estoque
        
        self.quantity = None # int
        
