#!/usr/bin/env python


class GetCategoriesResponse:

    def __init__(self):
        self.swaggerTypes = {
            'categories': 'list[Category]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'categories': 'categories',
            'metadata': 'metadata'
            
        }

        
        
        self.categories = None # list[Category]
        
        
        self.metadata = None # list[MetadataEntry]
        
