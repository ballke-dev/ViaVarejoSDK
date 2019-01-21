#!/usr/bin/env python


class Category:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'name': 'str',
            'parent_id': 'int',
            'items': 'int',
            'attributes': 'list[CategoryAttribute]',
            'categories': 'list[Category]'
            
        }

        self.attributeMap = {
            'id': 'id',
            'name': 'name',
            'parent_id': 'parentId',
            'items': 'items',
            'attributes': 'attributes',
            'categories': 'categories'
            
        }

        
        #ID da categoria
        
        self.id = None # int
        
        #Nome da categoria
        
        self.name = None # str
        
        #ID da categoria pai
        
        self.parent_id = None # int
        
        #Quantidade de produtos existentes nessa categoria
        
        self.items = None # int
        
        #Características do produto para a categoria
        
        self.attributes = None # list[CategoryAttribute]
        
        #Lista de sub-categorias (filhas)
        
        self.categories = None # list[Category]
        
