#!/usr/bin/env python


class OrderGiftWrap:

    def __init__(self):
        self.swaggerTypes = {
            'available': 'bool',
            'value': 'float',
            'message_support': 'bool',
            'gift_card': 'GiftCard'
            
        }

        self.attributeMap = {
            'available': 'available',
            'value': 'value',
            'message_support': 'messageSupport',
            'gift_card': 'giftCard'
            
        }

        
        #Flag que indica se existe embrulho para presente para o produto
        
        self.available = None # bool
        
        #Valor cobrado pelo embrulho
        
        self.value = None # float
        
        #Flag que indica se é possível incluir uma mensagem
        
        self.message_support = None # bool
        
        #Mensagem que deverá ser enviada juntamente com o embrulho de presente
        
        self.gift_card = None # GiftCard
        
