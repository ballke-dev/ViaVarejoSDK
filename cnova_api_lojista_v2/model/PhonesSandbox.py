#!/usr/bin/env python


class PhonesSandbox:

    def __init__(self):
        self.swaggerTypes = {
            'mobile': 'str',
            'home': 'str',
            'office': 'str'
            
        }

        self.attributeMap = {
            'mobile': 'mobile',
            'home': 'home',
            'office': 'office'
            
        }

        
        #Telefone celular do cliente
        
        self.mobile = None # str
        
        #Telefone residencial do cliente
        
        self.home = None # str
        
        #Telefone de trabalho do cliente
        
        self.office = None # str
        
