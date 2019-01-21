#!/usr/bin/env python


class CategoryAttribute:

    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'values': 'list[str]',
            'is_variant': 'bool'
            
        }

        self.attributeMap = {
            'name': 'name',
            'values': 'values',
            'is_variant': 'isVariant'
            
        }

        
        #Nome do atributo
        
        self.name = None # str
        
        #Lista de domínios para atributos variantes
        
        self.values = None # list[str]
        
        #Identifica se atributo pode sofrer variações
        
        self.is_variant = None # bool
        
