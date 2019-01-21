#!/usr/bin/env python


class Phone:

    def __init__(self):
        self.swaggerTypes = {
            'number': 'str',
            'type': 'str'
            
        }

        self.attributeMap = {
            'number': 'number',
            'type': 'type'
            
        }

        
        #Número do telefone
        
        self.number = None # str
        
        #Tipo do telefone
        
        self.type = None # str
        
