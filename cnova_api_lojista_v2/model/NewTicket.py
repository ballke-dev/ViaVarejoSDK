#!/usr/bin/env python


class NewTicket:

    def __init__(self):
        self.swaggerTypes = {
            'to': 'str',
            'body': 'str'
            
        }

        self.attributeMap = {
            'to': 'to',
            'body': 'body'
            
        }

        
        #Email do consumidor retornado no pedido
        
        self.to = None # str
        
        #Texto da mensagem
        
        self.body = None # str
        
