#!/usr/bin/env python


class OrdersTrackings:

    def __init__(self):
        self.swaggerTypes = {
            'trackings': 'list[OrderTracking]'
            
        }

        self.attributeMap = {
            'trackings': 'trackings'
            
        }

        
        #Lista de trackings
        
        self.trackings = None # list[OrderTracking]
        
