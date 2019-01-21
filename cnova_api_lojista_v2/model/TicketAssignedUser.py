#!/usr/bin/env python


class TicketAssignedUser:

    def __init__(self):
        self.swaggerTypes = {
            'user': 'str',
            'group': 'str'
            
        }

        self.attributeMap = {
            'user': 'user',
            'group': 'group'
            
        }

        
        #Identificador do assunto.
        
        self.user = None # str
        
        #Descrição do assunto relacionado ao ticket.
        
        self.group = None # str
        
