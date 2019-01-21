#!/usr/bin/env python


class TicketAssignee:

    def __init__(self):
        self.swaggerTypes = {
            'user': 'UserReference',
            'visibility': 'str',
            'body': 'str'
            
        }

        self.attributeMap = {
            'user': 'user',
            'visibility': 'visibility',
            'body': 'body'
            
        }

        
        #Dados do usuário que fará o atendimento do Ticket
        
        self.user = None # UserReference
        
        #Se for &#39;public&#39;, o consumidor poderá ver, se for private o consumidor não receberá a mensagem
        
        self.visibility = None # str
        
        #Mensagem a ser enviada como descrição da operação
        
        self.body = None # str
        
