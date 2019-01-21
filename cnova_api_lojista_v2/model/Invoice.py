#!/usr/bin/env python


class Invoice:

    def __init__(self):
        self.swaggerTypes = {
            'cnpj': 'str',
            'number': 'str',
            'serie': 'str',
            'issued_at': 'DateTime',
            'access_key': 'str',
            'link_xml': 'str',
            'link_danfe': 'str'
            
        }

        self.attributeMap = {
            'cnpj': 'cnpj',
            'number': 'number',
            'serie': 'serie',
            'issued_at': 'issuedAt',
            'access_key': 'accessKey',
            'link_xml': 'linkXml',
            'link_danfe': 'linkDanfe'
            
        }

        
        #CNPJ responsável pelo envio dos produtos. Pode ser diferente caso a empresa possua diversos Centros de Distribuição (CDs)
        
        self.cnpj = None # str
        
        #Número da Nota Fiscal
        
        self.number = None # str
        
        #Número de serie da Nota Fiscal
        
        self.serie = None # str
        
        #Data de emissão da Nota Fiscal
        
        self.issued_at = None # DateTime
        
        #Número da chave de acesso à nota fiscal. A chave possui 44 dígitos e contém todas as informações da DANFE
        
        self.access_key = None # str
        
        #Url para consulta da NFE
        
        self.link_xml = None # str
        
        #Url para consulta da DANFE
        
        self.link_danfe = None # str
        
