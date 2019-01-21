#!/usr/bin/env python


class NewTicketMessage:

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

        
        #Informações de usuário
        
        self.user = None # UserReference
        
        #Se o consumidor final irá receber/visualizar a mensagem. Os valores permitidos são: &#39;private&#39; e &#39;public&#39;
        
        self.visibility = None # str
        
        #Texto da mensagem
        
        self.body = None # str
        
