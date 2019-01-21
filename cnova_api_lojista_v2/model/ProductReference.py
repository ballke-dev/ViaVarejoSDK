#!/usr/bin/env python


class ProductReference:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'href': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'href': 'href'
            
        }

        
        #ID do recurso
        
        self.id = None # str
        
        #Link para acesso ao recurso
        
        self.href = None # str
        
