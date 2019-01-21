#!/usr/bin/env python


class ProductSiteReference:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'href': 'str',
            'site': 'str'
            
        }

        self.attributeMap = {
            'id': 'id',
            'href': 'href',
            'site': 'site'
            
        }

        
        #ID do produto
        
        self.id = None # str
        
        #Link do produto no site
        
        self.href = None # str
        
        #Site no qual o produto está disponível. Os possíveis sites são: &#39;EX&#39;, &#39;PF&#39;, &#39;CB&#39;, &#39;EH&#39;, &#39;BT&#39;, &#39;CD&#39;. Consulte a lista completa de sites disponíveis no serviço &lt;a href=&#39;#!/sites&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /sites&lt;/strong&gt;&lt;/a&gt;
        
        self.site = None # str
        
