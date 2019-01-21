#!/usr/bin/env python


class GetOrdersStatusNewResponse:

    def __init__(self):
        self.swaggerTypes = {
            'orders': 'list[OrderStatusNew]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'orders': 'orders',
            'metadata': 'metadata'
            
        }

        
        
        self.orders = None # list[OrderStatusNew]
        
        #Leia mais sobre os metadados retornados nas listagens em &lt;a href=&#39;../apis/index.html#search&#39; target=&#39;_blank&#39;&gt;Metadada&lt;/a&gt;
        
        self.metadata = None # list[MetadataEntry]
        
