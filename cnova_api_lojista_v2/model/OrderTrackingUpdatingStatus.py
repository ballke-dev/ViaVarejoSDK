#!/usr/bin/env python


class OrderTrackingUpdatingStatus:

    def __init__(self):
        self.swaggerTypes = {
            'order': 'OrderReference',
            'items': 'list[OrderItemReference]',
            'status': 'str',
            'processed_at': 'DateTime',
            'errors': 'list[Error]'
            
        }

        self.attributeMap = {
            'order': 'order',
            'items': 'items',
            'status': 'status',
            'processed_at': 'processedAt',
            'errors': 'errors'
            
        }

        
        #Dados do pedido
        
        self.order = None # OrderReference
        
        #Items do pedido
        
        self.items = None # list[OrderItemReference]
        
        #Status do pedido
        
        self.status = None # str
        
        #Data do processamento
        
        self.processed_at = None # DateTime
        
        #Erros do envido de pedidos
        
        self.errors = None # list[Error]
        
