#!/usr/bin/env python


class MetadataEntry:

    def __init__(self):
        self.swaggerTypes = {
            'key': 'str',
            'value': 'str'
            
        }

        self.attributeMap = {
            'key': 'key',
            'value': 'value'
            
        }

        
        #Chave de identificação do atributo
        
        self.key = None # str
        
        #Valor do atributo
        
        self.value = None # str
        
