#!/usr/bin/env python


class CustomerSandbox:

    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'gender': 'str',
            'document_number': 'str',
            'type': 'str',
            'email': 'str',
            'born_at': 'DateTime',
            'billing': 'BillingAddress',
            'phones': 'PhonesSandbox'
            
        }

        self.attributeMap = {
            'name': 'name',
            'gender': 'gender',
            'document_number': 'documentNumber',
            'type': 'type',
            'email': 'email',
            'born_at': 'bornAt',
            'billing': 'billing',
            'phones': 'phones'
            
        }

        
        #Nome do cliente
        
        self.name = None # str
        
        #Sexo - Masculino ou Feminino
        
        self.gender = None # str
        
        #Número de documento do cliente
        
        self.document_number = None # str
        
        #Tipo de cliente (Pessoa Física / Jurídica)
        
        self.type = None # str
        
        #Email do cliente
        
        self.email = None # str
        
        #Data de nascimento
        
        self.born_at = None # DateTime
        
        #Endereço do cliente
        
        self.billing = None # BillingAddress
        
        #Telefones do cliente
        
        self.phones = None # PhonesSandbox
        
