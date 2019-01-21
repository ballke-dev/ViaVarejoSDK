#!/usr/bin/env python


class Prices:

    def __init__(self):
        self.swaggerTypes = {
            'default': 'float',
            'offer': 'float',
            'site': 'str'
            
        }

        self.attributeMap = {
            'default': 'default',
            'offer': 'offer',
            'site': 'site'
            
        }

        
        #Preço de do produto no Marketplace
        
        self.default = None # float
        
        #Preço real de venda. Preço por do produto no Marketplace
        
        self.offer = None # float
        
        #Site no qual o preço será aplicado. Os possíveis sites são: &#39;EX&#39;, &#39;PF&#39;, &#39;CB&#39;, &#39;EH&#39;, &#39;BT&#39;, &#39;CD&#39;. Caso nenhum valor seja informado, será assumido o valor &#39;EX&#39; como padrão. Consulte a lista completa de sites disponíveis no serviço &lt;a href=&#39;#!/sites&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /sites&lt;/strong&gt;&lt;/a&gt;
        
        self.site = None # str
        
