#!/usr/bin/env python


class NewTracking:

    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[str]',
            'occurred_at': 'DateTime',
            'url': 'str',
            'number': 'str',
            'seller_delivery_id': 'str',
            'cte': 'str',
            'carrier': 'Carrier',
            'invoice': 'Invoice'
            
        }

        self.attributeMap = {
            'items': 'items',
            'occurred_at': 'occurredAt',
            'url': 'url',
            'number': 'number',
            'seller_delivery_id': 'sellerDeliveryId',
            'cte': 'cte',
            'carrier': 'carrier',
            'invoice': 'invoice'
            
        }

        
        #Lista de Order IDs dos produtos comprados no pedido e que irão ser atualizados pela operação de tracking
        
        self.items = None # list[str]
        
        #Data da ocorrência
        
        self.occurred_at = None # DateTime
        
        #Url para consulta na transportadora
        
        self.url = None # str
        
        #ID do objeto na transportadora
        
        self.number = None # str
        
        #ID de entrega do Lojista. Esse ID deve ser único para um pedido, não podendo haver repetição entre pedidos
        
        self.seller_delivery_id = None # str
        
        #Conhecimento do Transporte Eletrônico
        
        self.cte = None # str
        
        #Informações sobre a transportadora
        
        self.carrier = None # Carrier
        
        #Informações sobre a Nota Fiscal da compra
        
        self.invoice = None # Invoice
        
