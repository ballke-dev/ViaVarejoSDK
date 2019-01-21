#!/usr/bin/env python


class ProductLoadStock:

    def __init__(self):
        self.swaggerTypes = {
            'quantity': 'int',
            'cross_docking_time': 'int'
            
        }

        self.attributeMap = {
            'quantity': 'quantity',
            'cross_docking_time': 'crossDockingTime'
            
        }

        
        #Quantidade de produtos disponíveis
        
        self.quantity = None # int
        
        #Tempo de preparação/fabricação do produto em dias. Esse tempo é incluído no cálculo de frete
        
        self.cross_docking_time = None # int
        
