#!/usr/bin/env python


class Errors:

    def __init__(self):
        self.swaggerTypes = {
            'errors': 'list[Error]'
            
        }

        self.attributeMap = {
            'errors': 'errors'
            
        }

        
        #Lista contendo os skus que não puderam ser cancelado e o erro para cada um
        
        self.errors = None # list[Error]
        
