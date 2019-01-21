#!/usr/bin/env python


class Carrier:

    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'cnpj': 'str'
            
        }

        self.attributeMap = {
            'name': 'name',
            'cnpj': 'cnpj'
            
        }

        
        #Nome da transportadora
        
        self.name = None # str
        
        #CNPJ da transportadora
        
        self.cnpj = None # str
        
