#!/usr/bin/env python


class TicketSla:

    def __init__(self):
        self.swaggerTypes = {
            'expire_at': 'DateTime',
            'delayed': 'bool'
            
        }

        self.attributeMap = {
            'expire_at': 'expireAt',
            'delayed': 'delayed'
            
        }

        
        #Data de expiração para resolução do ticket.
        
        self.expire_at = None # DateTime
        
        #Indicador de atraso do ticket.
        
        self.delayed = None # bool
        
