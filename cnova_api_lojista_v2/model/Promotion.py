#!/usr/bin/env python


class Promotion:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'name': 'str',
            'amount': 'float',
            'type': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name',
            'amount': 'amount',
            'type': 'type'
            
        }

        
        #ID da promoção que o produto foi adquirido
        
        self.id = None # str
        
        #Descrição da promoção
        
        self.name = None # str
        
        #Total de desconto
        
        self.amount = None # float
        
        #Tipo da promoção
        
        self.type = None # str
        
