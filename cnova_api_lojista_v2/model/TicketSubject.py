#!/usr/bin/env python


class TicketSubject:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'name': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name'
            
        }

        
        #Identificador do assunto.
        
        self.id = None # int
        
        #Descrição do assunto relacionado ao ticket.
        
        self.name = None # str
        
