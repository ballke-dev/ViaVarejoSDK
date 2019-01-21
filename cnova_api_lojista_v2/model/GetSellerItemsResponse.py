#!/usr/bin/env python


class GetSellerItemsResponse:

    def __init__(self):
        self.swaggerTypes = {
            'seller_items': 'list[SellerItem]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'seller_items': 'sellerItems',
            'metadata': 'metadata'
            
        }

        
        
        self.seller_items = None # list[SellerItem]
        
        #Leia mais sobre os metadados retornados nas listagens em &lt;a href=&#39;../apis/index.html#search&#39; target=&#39;_blank&#39;&gt;Metadada&lt;/a&gt;
        
        self.metadata = None # list[MetadataEntry]
        
