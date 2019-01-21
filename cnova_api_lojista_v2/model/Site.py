#!/usr/bin/env python


class Site:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'name': 'str',
            'mnemonic': 'str',
            'url': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name',
            'mnemonic': 'mnemonic',
            'url': 'url'
            
        }

        
        #ID do site
        
        self.id = None # int
        
        #Nome do site
        
        self.name = None # str
        
        #Código que deverá ser utilizado nas operações que exigem o site. Exemplo: &lt;code&gt;GET /sellerItems?_offset=0&amp;_limit=10&amp;site=EX&lt;/code&gt; para trazer produtos vendidos apenas no Extra
        
        self.mnemonic = None # str
        
        #URL base para consultar produtos nesse site
        
        self.url = None # str
        
