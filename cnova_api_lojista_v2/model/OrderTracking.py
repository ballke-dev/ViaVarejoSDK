#!/usr/bin/env python


class OrderTracking:

    def __init__(self):
        self.swaggerTypes = {
            'order': 'OrderId',
            'items': 'list[OrderItemReference]',
            'control_point': 'str',
            'occurred_at': 'DateTime',
            'url': 'str',
            'number': 'str',
            'seller_delivery_id': 'str',
            'cte': 'str',
            'carrier': 'Carrier',
            'invoice': 'Invoice'
            
        }

        self.attributeMap = {
            'order': 'order',
            'items': 'items',
            'control_point': 'controlPoint',
            'occurred_at': 'occurredAt',
            'url': 'url',
            'number': 'number',
            'seller_delivery_id': 'sellerDeliveryId',
            'cte': 'cte',
            'carrier': 'carrier',
            'invoice': 'invoice'
            
        }

        
        #ID do pedido.
        
        self.order = None # OrderId
        
        #Itens do pedido
        
        self.items = None # list[OrderItemReference]
        
        #Status do pedido. Veja o serviço &lt;a href=&#39;#!/orders/getOrderByIdV2_get_0&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /orders/{orderId}&lt;/strong&gt;&lt;/a&gt; para consultar todos os controlPoits existentes.
        
        self.control_point = None # str
        
        #Data da ocorrencia
        
        self.occurred_at = None # DateTime
        
        #Url para consulta na transportadora
        
        self.url = None # str
        
        #ID do objeto na transportadora
        
        self.number = None # str
        
        #ID único da entrega para o lojista no parceiro, não pode haver repetição deste ID
        
        self.seller_delivery_id = None # str
        
        #Conhecimento de Transporte Eletôniconico
        
        self.cte = None # str
        
        #Informações da Transportadora
        
        self.carrier = None # Carrier
        
        #Informações sobre a Nota Fiscal de compra
        
        self.invoice = None # Invoice
        
