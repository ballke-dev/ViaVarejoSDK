#!/usr/bin/env python


class Ticket:

    def __init__(self):
        self.swaggerTypes = {
            'code': 'str',
            'status': 'str',
            'description': 'str',
            'created_at': 'DateTime',
            'updated_at': 'DateTime',
            'closed_at': 'DateTime',
            'priority': 'str',
            'assignee': 'TicketAssignedUser',
            'ombudsman': 'Ombudsman',
            'customer': 'CustomerReference',
            'site': 'str',
            'channel': 'str',
            'type': 'TicketType',
            'subject': 'TicketSubject',
            'sla': 'TicketSla',
            'metadata': 'list[MetadataEntry]'
            
        }

        self.attributeMap = {
            'code': 'code',
            'status': 'status',
            'description': 'description',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'closed_at': 'closedAt',
            'priority': 'priority',
            'assignee': 'assignee',
            'ombudsman': 'ombudsman',
            'customer': 'customer',
            'site': 'site',
            'channel': 'channel',
            'type': 'type',
            'subject': 'subject',
            'sla': 'sla',
            'metadata': 'metadata'
            
        }

        
        #ID do ticket
        
        self.code = None # str
        
        #Status do ticket que são classificados como: &lt;strong&gt;&#39;opened&#39;, &#39;closed&#39; e &#39;attendance&#39;.&lt;/strong&gt;
        
        self.status = None # str
        
        #Descrição do ticket
        
        self.description = None # str
        
        #Data da criação do ticket
        
        self.created_at = None # DateTime
        
        #Atualização do ticket
        
        self.updated_at = None # DateTime
        
        #Data de encerramento do ticket
        
        self.closed_at = None # DateTime
        
        #Prioridade do ticket possui os seguintes valores: &lt;strong&gt;&#39;Normal&#39; e &#39;Em Acompanhamento&#39;&lt;/strong&gt;
        
        self.priority = None # str
        
        #Responsável pelo atendimento do protocolo.
        
        self.assignee = None # TicketAssignedUser
        
        #Informações de ouvidoria
        
        self.ombudsman = None # Ombudsman
        
        #Cliente associado ao ticket
        
        self.customer = None # CustomerReference
        
        #Site de origem do protocolo. Os valores disponíveis no site são: &lt;strong&gt; CD, BT, EH, EX, PF, e CB &lt;/strong&gt;
        
        self.site = None # str
        
        #O canal de atendimento de origem do protocolo, possui os seguintes valores: &lt;strong&gt; Fale Conosco, Admin Seller, CallCenter, Email, e External Service&lt;/strong&gt;
        
        self.channel = None # str
        
        #Tipo do ticket.
        
        self.type = None # TicketType
        
        #Assunto relacionado ao ticket.
        
        self.subject = None # TicketSubject
        
        #Informações sobre o prazo de atendimento do ticket.
        
        self.sla = None # TicketSla
        
        #Leia mais sobre os metadados retornados nas listagens em &lt;a href=&#39;../apis/index.html#search&#39;&gt;Metadada&lt;/a&gt;
        
        self.metadata = None # list[MetadataEntry]
        
