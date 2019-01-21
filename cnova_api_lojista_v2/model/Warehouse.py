#!/usr/bin/env python


class Warehouse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'sites': 'list[str]'
            
        }

        self.attributeMap = {
            'id': 'id',
            'sites': 'sites'
            
        }

        
        #ID do warehouse. Ele deve ser utilizado nas atualizações de estoque dos produtos.
        
        self.id = None # int
        
        #Lista de sites que esse warehouse atende.
        
        self.sites = None # list[str]
        
