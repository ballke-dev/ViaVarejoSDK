#!/usr/bin/env python


class GetOrdersTrackingUpdatingResponse:

    def __init__(self):
        self.swaggerTypes = {
            'trackings': 'list[OrderTrackingUpdatingStatus]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'trackings': 'trackings',
            'metadata': 'metadata'
            
        }

        
        #Informações de tracking do pedido
        
        self.trackings = None # list[OrderTrackingUpdatingStatus]
        
        #Dados adicionais da consulta
        
        self.metadata = None # list[MetadataEntry]
        
