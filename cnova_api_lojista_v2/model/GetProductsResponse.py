#!/usr/bin/env python


class GetProductsResponse:

    def __init__(self):
        self.swaggerTypes = {
            'skus': 'list[ProductResponseItem]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'skus': 'skus',
            'metadata': 'metadata'
            
        }

        
        
        self.skus = None # list[ProductResponseItem]
        
        #Dados adicionais da consulta
        
        self.metadata = None # list[MetadataEntry]
        
