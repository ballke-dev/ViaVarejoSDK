#!/usr/bin/env python


class GiftWrap:

    def __init__(self):
        self.swaggerTypes = {
            'available': 'bool',
            'value': 'float',
            'message_support': 'bool'
            
        }

        self.attributeMap = {
            'available': 'available',
            'value': 'value',
            'message_support': 'messageSupport'
            
        }

        
        #Flag que indica se existe embrulho para presente para o produto
        
        self.available = None # bool
        
        #Valor cobrado pelo embrulho
        
        self.value = None # float
        
        #Flag que indica se é possível incluir uma mensagem
        
        self.message_support = None # bool
        
