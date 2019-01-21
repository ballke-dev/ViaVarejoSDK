#!/usr/bin/env python


class TicketType:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'name': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name'
            
        }

        
        #Identificador do tipo de ticket.
        
        self.id = None # int
        
        #Descrição do tipo de ticket com a ação esperada.
        
        self.name = None # str
        
