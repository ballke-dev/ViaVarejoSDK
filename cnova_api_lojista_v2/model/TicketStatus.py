#!/usr/bin/env python


class TicketStatus:

    def __init__(self):
        self.swaggerTypes = {
            'ticket_status': 'str'
            
        }

        self.attributeMap = {
            'ticket_status': 'ticketStatus'
            
        }

        
        #Novo status desejado do Ticket. Fechado &lt;strong&gt; (closed) &lt;/strong&gt; e Em Acompanhamento &lt;strong&gt; (attendance) &lt;/strong&gt;
        
        self.ticket_status = None # str
        
