#!/usr/bin/env python


class ItemTracking:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'href': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'href': 'href'
            
        }

        
        #Order Item ID do produto vendido
        
        self.id = None # str
        
        #Link para acesso ao item
        
        self.href = None # str
        
