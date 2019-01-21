#!/usr/bin/env python


class SellerItemPrices:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'prices': 'list[Prices]'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'prices': 'prices'
            
        }

        
        #SKU do produto do lojista que deverá ser alterado
        
        self.sku_seller_id = None # str
        
        #Preço do produto
        
        self.prices = None # list[Prices]
        
