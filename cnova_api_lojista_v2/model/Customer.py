#!/usr/bin/env python


class Customer:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'name': 'str',
            'document_number': 'str',
            'type': 'str',
            'created_at': 'DateTime',
            'email': 'str',
            'birth_date': 'DateTime',
            'phones': 'list[Phone]'
            
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name',
            'document_number': 'documentNumber',
            'type': 'type',
            'created_at': 'createdAt',
            'email': 'email',
            'birth_date': 'birthDate',
            'phones': 'phones'
            
        }

        
        #Identificador do cliente
        
        self.id = None # str
        
        #Nome completo do cliente
        
        self.name = None # str
        
        #Documento do cliente
        
        self.document_number = None # str
        
        #Tipo de cliente: Pessoa Física ou Jurídica
        
        self.type = None # str
        
        #Data de envio do produto
        
        self.created_at = None # DateTime
        
        #Email do cliente
        
        self.email = None # str
        
        #Data de nascimento do cliente
        
        self.birth_date = None # DateTime
        
        #Lista de telefones do cliente
        
        self.phones = None # list[Phone]
        
