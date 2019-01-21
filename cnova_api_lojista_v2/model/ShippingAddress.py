#!/usr/bin/env python


class ShippingAddress:

    def __init__(self):
        self.swaggerTypes = {
            'address': 'str',
            'number': 'str',
            'complement': 'str',
            'quarter': 'str',
            'reference': 'str',
            'city': 'str',
            'state': 'str',
            'country_id': 'str',
            'zip_code': 'str',
            'recipient_name': 'str'
            
        }

        self.attributeMap = {
            'address': 'address',
            'number': 'number',
            'complement': 'complement',
            'quarter': 'quarter',
            'reference': 'reference',
            'city': 'city',
            'state': 'state',
            'country_id': 'countryId',
            'zip_code': 'zipCode',
            'recipient_name': 'recipientName'
            
        }

        
        #Endereço (nome da rua, avenida ... )
        
        self.address = None # str
        
        #Número do endereço
        
        self.number = None # str
        
        #Informações adicionais
        
        self.complement = None # str
        
        #Bairro
        
        self.quarter = None # str
        
        #Pontos de referência
        
        self.reference = None # str
        
        #Cidade
        
        self.city = None # str
        
        #Estado
        
        self.state = None # str
        
        #Identificação do País. Baseado na ISO-3166, padrão alpha 2. Ex.: BR, US, AR
        
        self.country_id = None # str
        
        #Código de Endereçamento Postal - CEP
        
        self.zip_code = None # str
        
        #Nome do destinatario
        
        self.recipient_name = None # str
        
