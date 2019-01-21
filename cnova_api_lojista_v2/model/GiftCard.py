#!/usr/bin/env python


class GiftCard:

    def __init__(self):
        self.swaggerTypes = {
            '_from': 'str',
            'to': 'str',
            'message': 'str'
            
        }

        self.attributeMap = {
            '_from': 'from',
            'to': 'to',
            'message': 'message'
            
        }

        
        #Nome de quem está dando o presente
        
        self._from = None # str
        
        #Nome de quem irá receber o presente
        
        self.to = None # str
        
        #Mensagem que deverá ser enviada no cartão juntamente com o embrulho de presente
        
        self.message = None # str
        
