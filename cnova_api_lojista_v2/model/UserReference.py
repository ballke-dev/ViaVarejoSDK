#!/usr/bin/env python


class UserReference:

    def __init__(self):
        self.swaggerTypes = {
            'login': 'str',
            'name': 'str'
            
        }

        self.attributeMap = {
            'login': 'login',
            'name': 'name'
            
        }

        
        #Login do usuário que fará o atendimento do Ticket
        
        self.login = None # str
        
        #Nome do usuário que fará o atendimento do Ticket
        
        self.name = None # str
        
