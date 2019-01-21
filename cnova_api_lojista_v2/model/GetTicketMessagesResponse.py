#!/usr/bin/env python


class GetTicketMessagesResponse:

    def __init__(self):
        self.swaggerTypes = {
            'messages': 'list[TicketMessage]',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'messages': 'messages',
            'metadata': 'metadata'
            
        }

        
        #Mensagens
        
        self.messages = None # list[TicketMessage]
        
        #Metadados do status
        
        self.metadata = None # list[MetadataEntry]
        
