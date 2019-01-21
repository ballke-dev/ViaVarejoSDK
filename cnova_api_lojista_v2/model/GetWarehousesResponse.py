#!/usr/bin/env python


class GetWarehousesResponse:

    def __init__(self):
        self.swaggerTypes = {
            'warehouses': 'list[Warehouse]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'warehouses': 'warehouses',
            'metadata': 'metadata'
            
        }

        
        
        self.warehouses = None # list[Warehouse]
        
        
        self.metadata = None # list[MetadataEntry]
        
