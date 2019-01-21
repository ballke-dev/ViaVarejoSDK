#!/usr/bin/env python


class Image:

    def __init__(self):
        self.swaggerTypes = {
            'type': 'str',
            'main': 'bool',
            'url': 'str'
            
        }

        self.attributeMap = {
            'type': 'type',
            'main': 'main',
            'url': 'url'
            
        }

        
        #Formato da imagem
        
        self.type = None # str
        
        #Flag que indica se a imagem é a principal
        
        self.main = None # bool
        
        #URL da imagem do produto
        
        self.url = None # str
        
