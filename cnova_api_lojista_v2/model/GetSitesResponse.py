#!/usr/bin/env python


class GetSitesResponse:

    def __init__(self):
        self.swaggerTypes = {
            'total_rows': 'int',
            'sites': 'list[Site]'
            
        }

        self.attributeMap = {
            'total_rows': 'totalRows',
            'sites': 'sites'
            
        }

        
        
        self.total_rows = None # int
        
        
        self.sites = None # list[Site]
        
