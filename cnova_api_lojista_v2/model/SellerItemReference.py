#!/usr/bin/env python


class SellerItemReference:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'href': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'href': 'href'
            
        }

        
        #ID do produto
        
        self.id = None # str
        
        #Caminho do produto
        
        self.href = None # str
        
