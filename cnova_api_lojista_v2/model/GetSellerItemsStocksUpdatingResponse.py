#!/usr/bin/env python


class GetSellerItemsStocksUpdatingResponse:

    def __init__(self):
        self.swaggerTypes = {
            'skus': 'list[StockUpdatingStatus]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'skus': 'skus',
            'metadata': 'metadata'
            
        }

        
        #Lista de produtos e seus respectivos processos de atualização de estoque
        
        self.skus = None # list[StockUpdatingStatus]
        
        #Dados adicionais da consulta
        
        self.metadata = None # list[MetadataEntry]
        
