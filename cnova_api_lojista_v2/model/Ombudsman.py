#!/usr/bin/env python


class Ombudsman:

    def __init__(self):
        self.swaggerTypes = {
            'active': 'bool',
            'source': 'str',
            'created_at': 'DateTime'
            
        }

        self.attributeMap = {
            'active': 'active',
            'source': 'source',
            'created_at': 'createdAt'
            
        }

        
        #Quando for &#39;true&#39; se o protocolo estiver na Ouvidoria, e &#39;false&#39; se não estiver
        
        self.active = None # bool
        
        #Quando um protocolo está como ouvidoria com valor &#39;true&#39; os possíveis valores são: Facebook / Procon / Reclameaqui / Twitter / Outros.
        
        self.source = None # str
        
        #Data de entrada na Ouvidoria
        
        self.created_at = None # DateTime
        
