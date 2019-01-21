#!/usr/bin/env python


class TicketMessage:

    def __init__(self):
        self.swaggerTypes = {
            'created_at': 'DateTime',
            'id': 'str',
            'user': 'UserReference',
            'body': 'str',
            'visibility': 'str'
            
        }

        self.attributeMap = {
            'created_at': 'createdAt',
            'id': 'id',
            'user': 'user',
            'body': 'body',
            'visibility': 'visibility'
            
        }

        
        #Data de criação do Ticket
        
        self.created_at = None # DateTime
        
        #Id do Ticket
        
        self.id = None # str
        
        #Usuário
        
        self.user = None # UserReference
        
        #Texto da mensagem
        
        self.body = None # str
        
        #Se o consumidor final irá receber/visualizar a mensagem. Os valores permitidos são: &#39;private&#39; e &#39;public&#39;
        
        self.visibility = None # str
        
