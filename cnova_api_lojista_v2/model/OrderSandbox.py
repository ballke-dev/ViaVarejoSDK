#!/usr/bin/env python


class OrderSandbox:

    def __init__(self):
        self.swaggerTypes = {
            'site': 'str',
            'items': 'list[OrderItemSandbox]',
            'customer': 'CustomerSandbox'
            
        }

        self.attributeMap = {
            'site': 'site',
            'items': 'items',
            'customer': 'customer'
            
        }

        
        #Site para o qual o pedido será criado. . Consulte a lista completa de sites disponíveis no serviço &lt;a href=&#39;#!/sites&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /sites&lt;/strong&gt;&lt;/a&gt;
        
        self.site = None # str
        
        #Lista de produtos do pedido
        
        self.items = None # list[OrderItemSandbox]
        
        #Informações do cliente
        
        self.customer = None # CustomerSandbox
        
