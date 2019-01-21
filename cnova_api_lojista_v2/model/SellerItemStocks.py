#!/usr/bin/env python


class SellerItemStocks:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'stocks': 'list[Stock]'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'stocks': 'stocks'
            
        }

        
        #SKU do produto do lojista que deverá ser alterado
        
        self.sku_seller_id = None # str
        
        #Estoque do produto
        
        self.stocks = None # list[Stock]
        
