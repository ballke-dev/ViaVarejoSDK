#!/usr/bin/env python


class ProductLoadPrices:

    def __init__(self):
        self.swaggerTypes = {
            'default': 'float',
            'offer': 'float'
            
        }

        self.attributeMap = {
            'default': 'default',
            'offer': 'offer'
            
        }

        
        #Preço de do produto no Marketplace
        
        self.default = None # float
        
        #Preço real de venda. Preço por do produto no Marketplace
        
        self.offer = None # float
        
