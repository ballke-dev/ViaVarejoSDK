#!/usr/bin/env python


class OrderStatusNew:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'order_site_id': 'str',
            'site': 'str',
            'payment_type': 'int',
            'purchased_at': 'DateTime',
            'approved_at': 'DateTime',
            'updated_at': 'DateTime',
            'status': 'str',
            'total_amount': 'float',
            'total_discount_amount': 'float',
            'billing': 'BillingAddress',
            'customer': 'Customer',
            'freight': 'Freight',
            'items': 'list[OrderItem]',
            'trackings': 'list[Tracking]',
            'seller': 'Seller'
            
        }

        self.attributeMap = {
            'id': 'id',
            'order_site_id': 'orderSiteId',
            'site': 'site',
            'payment_type': 'paymentType',
            'purchased_at': 'purchasedAt',
            'approved_at': 'approvedAt',
            'updated_at': 'updatedAt',
            'status': 'status',
            'total_amount': 'totalAmount',
            'total_discount_amount': 'totalDiscountAmount',
            'billing': 'billing',
            'customer': 'customer',
            'freight': 'freight',
            'items': 'items',
            'trackings': 'trackings',
            'seller': 'seller'
            
        }

        
        #ID do pedido gerado para o lojista
        
        self.id = None # str
        
        #ID do pedido gerado no site e que é passado ao cliente
        
        self.order_site_id = None # str
        
        #Site para o qual o pedido foi criado. Consulte a lista completa de sites disponíveis no serviço &lt;a href=&#39;#!/sites&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /sites&lt;/strong&gt;&lt;/a&gt;
        
        self.site = None # str
        
        #Código do meio de pagamento. Consulte todos os tipos de pagamento disponíveis em &lt;a href=&#39;#!/orders/getOrderByIdV2_get_0&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /orders/{orderId}&lt;/strong&gt;&lt;/a&gt;
        
        self.payment_type = None # int
        
        #Data da compra
        
        self.purchased_at = None # DateTime
        
        #Data de aprovação de pagamento do pedido
        
        self.approved_at = None # DateTime
        
        #Última data de atualização do pedido
        
        self.updated_at = None # DateTime
        
        #Status atual do pedido
        
        self.status = None # str
        
        #Total do pedido
        
        self.total_amount = None # float
        
        #Total de descontos do pedido
        
        self.total_discount_amount = None # float
        
        #Informações de cobrança
        
        self.billing = None # BillingAddress
        
        #Informações do cliente
        
        self.customer = None # Customer
        
        #Informações de frete do pedido
        
        self.freight = None # Freight
        
        #Lista de itens do pedido
        
        self.items = None # list[OrderItem]
        
        #Informações de tracking do pedido
        
        self.trackings = None # list[Tracking]
        
        #Informações de venda
        
        self.seller = None # Seller
        
