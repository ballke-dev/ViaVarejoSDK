#!/usr/bin/env python


class OrderItemSandbox:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'name': 'str',
            'sale_price': 'float',
            'quantity': 'int'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'name': 'name',
            'sale_price': 'salePrice',
            'quantity': 'quantity'
            
        }

        
        #SKU ID do produto do Lojista
        
        self.sku_seller_id = None # str
        
        #Nome do produto
        
        self.name = None # str
        
        #Preço de venda
        
        self.sale_price = None # float
        
        #Quantidade produtos
        
        self.quantity = None # int
        
