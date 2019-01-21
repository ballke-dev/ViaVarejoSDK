#!/usr/bin/env python


class Tickets:

    def __init__(self):
        self.swaggerTypes = {
            'tickets': 'list[Ticket]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'tickets': 'tickets',
            'metadata': 'metadata'
            
        }

        
        #Tickets
        
        self.tickets = None # list[Ticket]
        
        #Leia mais sobre os metadados retornados nas listagens em &lt;a href=&#39;../apis/index.html#search&#39;&gt;Metadada&lt;/a&gt;
        
        self.metadata = None # list[MetadataEntry]
        
