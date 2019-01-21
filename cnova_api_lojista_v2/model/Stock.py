#!/usr/bin/env python


class Stock:

    def __init__(self):
        self.swaggerTypes = {
            'quantity': 'int',
            'cross_docking_time': 'int',
            'warehouse': 'int'
            
        }

        self.attributeMap = {
            'quantity': 'quantity',
            'cross_docking_time': 'crossDockingTime',
            'warehouse': 'warehouse'
            
        }

        
        #Quantidade de produtos disponíveis
        
        self.quantity = None # int
        
        #Tempo de preparação/fabricação do produto em dias. Esse tempo é incluído no cálculo de frete
        
        self.cross_docking_time = None # int
        
        #ID do depósito no qual o estoque do produto está sendo considerado. Consulte a lista completa de warehouses disponíveis no serviço &lt;a href=&#39;#!/warehouses&#39; target=&#39;_blank&#39;&gt;&lt;strong&gt;GET /warehouses&lt;/strong&gt;&lt;/a&gt;
        
        self.warehouse = None # int
        
