#!/usr/bin/env python


class GetSellerItemsPricesUpdatingResponse:

    def __init__(self):
        self.swaggerTypes = {
            'skus': 'list[PricesUpdatingStatus]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'skus': 'skus',
            'metadata': 'metadata'
            
        }

        
        #Skus do pedido
        
        self.skus = None # list[PricesUpdatingStatus]
        
        #Dados adicionais da consulta
        
        self.metadata = None # list[MetadataEntry]
        
