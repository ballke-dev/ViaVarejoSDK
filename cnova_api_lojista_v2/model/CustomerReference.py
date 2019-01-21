#!/usr/bin/env python


class CustomerReference:

    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'phone_number': 'str'
            
        }

        self.attributeMap = {
            'name': 'name',
            'phone_number': 'phoneNumber'
            
        }

        
        #Nome do cliente
        
        self.name = None # str
        
        #Telefone do cliente
        
        self.phone_number = None # str
        
