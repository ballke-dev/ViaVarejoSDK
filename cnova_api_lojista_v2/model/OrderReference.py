#!/usr/bin/env python


class OrderReference:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'href': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'href': 'href'
            
        }

        
        #ID do pedido.
        
        self.id = None # int
        
        #URL de consulta da ordem por ID.
        
        self.href = None # str
        
