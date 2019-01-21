#!/usr/bin/env python


class SellerItem:

    def __init__(self):
        self.swaggerTypes = {
            'sku_seller_id': 'str',
            'sku_site_id': 'str',
            'title': 'str',
            'brand': 'str',
            'gtin': 'list[str]',
            'status': 'list[SellerItemStatus]',
            'prices': 'list[Prices]',
            'stocks': 'list[ControlledStock]',
            'urls': 'list[ProductSiteReference]',
            'images': 'list[Image]',
            'product': 'ProductReference',
            'dimensions': 'Dimensions',
            'gift_wrap': 'GiftWrap',
            'attributes': 'list[ProductAttribute]'
            
        }

        self.attributeMap = {
            'sku_seller_id': 'skuSellerId',
            'sku_site_id': 'skuSiteId',
            'title': 'title',
            'brand': 'brand',
            'gtin': 'gtin',
            'status': 'status',
            'prices': 'prices',
            'stocks': 'stocks',
            'urls': 'urls',
            'images': 'images',
            'product': 'product',
            'dimensions': 'dimensions',
            'gift_wrap': 'giftWrap',
            'attributes': 'attributes'
            
        }

        
        #SKU ID do produto do Lojista
        
        self.sku_seller_id = None # str
        
        #SKU Id do produto do Extra.
        
        self.sku_site_id = None # str
        
        #Título de venda do produto no Marketplace. Ex Televisor de LCD Sony Bravia 40...
        
        self.title = None # str
        
        #Marca do produto. Ex Sony
        
        self.brand = None # str
        
        #Lista que pode conter tanto o código EAN do produto (código de barras) quanto códigos ISBN (geralmente utilizados para livros)
        
        self.gtin = None # list[str]
        
        #Status do produto para cada site
        
        self.status = None # list[SellerItemStatus]
        
        #Informações de preço de venda do produto para cada site
        
        self.prices = None # list[Prices]
        
        #Informações de estoque do produto para cada site
        
        self.stocks = None # list[ControlledStock]
        
        #Lista de urls do produto para cada site no qual o mesmo está disponível
        
        self.urls = None # list[ProductSiteReference]
        
        #Lista de imagens do produto
        
        self.images = None # list[Image]
        
        #Informações do catálogo de produtos
        
        self.product = None # ProductReference
        
        #Informações de dimensões do produto
        
        self.dimensions = None # Dimensions
        
        #Informações de embrulho para presente
        
        self.gift_wrap = None # GiftWrap
        
        #Características do produto
        
        self.attributes = None # list[ProductAttribute]
        
