#!/usr/bin/env python


class Freight:

    def __init__(self):
        self.swaggerTypes = {
            'actual_amount': 'float',
            'charged_amount': 'float',
            'transit_time': 'int',
            'cross_docking_time': 'int',
            'additional_info': 'str',
            'type': 'str',
            'scheduled_at': 'DateTime',
            'scheduled_period': 'str'
            
        }

        self.attributeMap = {
            'actual_amount': 'actualAmount',
            'charged_amount': 'chargedAmount',
            'transit_time': 'transitTime',
            'cross_docking_time': 'crossDockingTime',
            'additional_info': 'additionalInfo',
            'type': 'type',
            'scheduled_at': 'scheduledAt',
            'scheduled_period': 'scheduledPeriod'
            
        }

        
        #Valor nominal do frete (sem descontos e abatimentos, com margem comercial)
        
        self.actual_amount = None # float
        
        #Valor cobrado pelo frete
        
        self.charged_amount = None # float
        
        #Prazo de transporte para entrega do produto em dias úteis
        
        self.transit_time = None # int
        
        #Tempo de preparação/fabricação do produto em dias. Esse tempo é incluído no cálculo de frete.
        
        self.cross_docking_time = None # int
        
        #Informações adicionais sobre a entrega. Pode ser utilizado para informar o nome da transportadora, por exemplo
        
        self.additional_info = None # str
        
        #Tipo de frete
        
        self.type = None # str
        
        #Data de agendamento da entrega
        
        self.scheduled_at = None # DateTime
        
        #Período que a entrega foi agendada
        
        self.scheduled_period = None # str
        
