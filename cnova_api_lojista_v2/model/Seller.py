#!/usr/bin/env python


class Seller:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'name': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name'
            
        }

        
        #ID do produto
        
        self.id = None # str
        
        #Nome do produto
        
        self.name = None # str
        
