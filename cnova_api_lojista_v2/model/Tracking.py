#!/usr/bin/env python


class Tracking:

    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[ItemTracking]',
            'control_point': 'str',
            'description': 'str',
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
            'control_point': 'controlPoint',
            'description': 'description',
            'occurred_at': 'occurredAt',
            'url': 'url',
            'number': 'number',
            'seller_delivery_id': 'sellerDeliveryId',
            'cte': 'cte',
            'carrier': 'carrier',
            'invoice': 'invoice'
            
        }

        
        #Lista de itens alterados pela operação de tracking
        
        self.items = None # list[ItemTracking]
        
        #Status do pedido. Veja o serviço &lt;a href=&#39;#!/orders/getOrderByIdV2_get_0&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /orders/{orderId}&lt;/strong&gt;&lt;/a&gt; para consultar todos os controlPoits existentes.
        
        self.control_point = None # str
        
        #Descrição adicional sobre tracking
        
        self.description = None # str
        
        #Data da ocorrência
        
        self.occurred_at = None # DateTime
        
        #Url para consulta na transportadora
        
        self.url = None # str
        
        #ID do objeto na transportadora
        
        self.number = None # str
        
        #ID único da entrega para o lojista no parceiro, não pode haver repetição deste ID
        
        self.seller_delivery_id = None # str
        
        #Conhecimento de Transporte Eletrônico
        
        self.cte = None # str
        
        #Informações sobre transportadora
        
        self.carrier = None # Carrier
        
        #Informações sobre a Nota Fiscal da compra
        
        self.invoice = None # Invoice
        
