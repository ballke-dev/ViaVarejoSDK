#!/usr/bin/env python


class SellerItemStatus:

    def __init__(self):
        self.swaggerTypes = {
            'active': 'bool',
            'site': 'str'
            
        }

        self.attributeMap = {
            'active': 'active',
            'site': 'site'
            
        }

        
        #Indica se o produto está ativo &#39;TRUE&#39; (à venda no MP) ou não &#39;FALSE&#39;
        
        self.active = None # bool
        
        #Site para o qual o status é considerado. Os possíveis sites são: &#39;EX&#39;,&#39;PF&#39;,&#39;CB&#39;, &#39;EH&#39;, &#39;BT&#39;, &#39;CD&#39;.
        
        self.site = None # str
        
