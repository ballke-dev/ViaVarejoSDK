#!/usr/bin/env python


class GetSellerItemsStatusUpdatingResponse:

    def __init__(self):
        self.swaggerTypes = {
            'skus': 'list[SellerItemStatusUpdatingStatus]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'skus': 'skus',
            'metadata': 'metadata'
            
        }

        
        #Informações de status de SKU do produto do lojista
        
        self.skus = None # list[SellerItemStatusUpdatingStatus]
        
        #Dados adicionais da consulta
        
        self.metadata = None # list[MetadataEntry]
        
