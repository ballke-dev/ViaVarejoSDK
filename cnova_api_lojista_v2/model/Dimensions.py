#!/usr/bin/env python


class Dimensions:

    def __init__(self):
        self.swaggerTypes = {
            'weight': 'float',
            'length': 'float',
            'width': 'float',
            'height': 'float'
            
        }

        self.attributeMap = {
            'weight': 'weight',
            'length': 'length',
            'width': 'width',
            'height': 'height'
            
        }

        
        #Peso do produto, em quilos. Não pode ser 0 (zero) e deve ter no máximo duas casas decimais
        
        self.weight = None # float
        
        #Comprimento do produto, em metros. Não pode ser 0 (zero) e deve ter no máximo duas casas decimais
        
        self.length = None # float
        
        #Largura do produto, em metros. Não pode ser 0 (zero) e deve ter no máximo duas casas decimais
        
        self.width = None # float
        
        #Altura do produto, em metros. Não pode ser 0 (zero) e deve ter no máximo duas casas decimais
        
        self.height = None # float
        
