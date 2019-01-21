#!/usr/bin/env python


class OrderItem:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'sku_seller_id': 'str',
            'name': 'str',
            'sale_price': 'float',
            'sent': 'bool',
            'freight': 'Freight',
            'gift_wrap': 'OrderGiftWrap',
            'promotions': 'list[Promotion]'
            
        }

        self.attributeMap = {
            'id': 'id',
            'sku_seller_id': 'skuSellerId',
            'name': 'name',
            'sale_price': 'salePrice',
            'sent': 'sent',
            'freight': 'freight',
            'gift_wrap': 'giftWrap',
            'promotions': 'promotions'
            
        }

        
        #ID do item de Pedido
        
        self.id = None # str
        
        #SKU ID do produto do Lojista
        
        self.sku_seller_id = None # str
        
        #Nome do produto
        
        self.name = None # str
        
        #Preço de venda unitário
        
        self.sale_price = None # float
        
        #Flag que indica se o produto já foi enviado
        
        self.sent = None # bool
        
        #Informações sobre o frete do produto
        
        self.freight = None # Freight
        
        #Informações de embrulho para presente
        
        self.gift_wrap = None # OrderGiftWrap
        
        #Lista de Promoções
        
        self.promotions = None # list[Promotion]
        
