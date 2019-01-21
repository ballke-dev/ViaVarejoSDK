#!/usr/bin/env python


class ProductAttribute:

    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'value': 'str'
            
        }

        self.attributeMap = {
            'name': 'name',
            'value': 'value'
            
        }

        
        #Nome do atributo
        
        self.name = None # str
        
        #Valor do atributo
        
        self.value = None # str
        
