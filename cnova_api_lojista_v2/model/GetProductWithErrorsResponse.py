#!/usr/bin/env python


class GetProductWithErrorsResponse:

    def __init__(self):
        self.swaggerTypes = {
            'sku_id': 'str',
            'sku_seller_id': 'str',
            'product_seller_id': 'str',
            'title': 'str',
            'description': 'str',
            'brand': 'str',
            'gtin': 'list[str]',
            'categories': 'list[str]',
            'images': 'list[str]',
            'videos': 'list[str]',
            'price': 'ProductLoadPrices',
            'stock': 'ProductLoadStock',
            'dimensions': 'Dimensions',
            'gift_wrap': 'GiftWrap',
            'attributes': 'list[ProductAttribute]',
            'errors': 'list[Error]'
            
        }

        self.attributeMap = {
            'sku_id': 'skuId',
            'sku_seller_id': 'skuSellerId',
            'product_seller_id': 'productSellerId',
            'title': 'title',
            'description': 'description',
            'brand': 'brand',
            'gtin': 'gtin',
            'categories': 'categories',
            'images': 'images',
            'videos': 'videos',
            'price': 'price',
            'stock': 'stock',
            'dimensions': 'dimensions',
            'gift_wrap': 'giftWrap',
            'attributes': 'attributes',
            'errors': 'errors'
            
        }

        
        #SKU ID do produto no Marketplace - utilizado para realizar associação de produtos
        
        self.sku_id = None # str
        
        #SKU ID do produto do Lojista
        
        self.sku_seller_id = None # str
        
        #ID do produto do lojista para fazer o agrupamento de SKUs
        
        self.product_seller_id = None # str
        
        #Nome no Marketplace. Ex Televisor de LCD Sony Bravia 40...
        
        self.title = None # str
        
        #Descrição do produto. Aceita tags HTML para formatar a apresentação da descrição, no entanto há alguma tags restritas (tags para acesso a conteúdo externo): img, object, script e iframe.
        
        self.description = None # str
        
        #Marca. Ex Sony
        
        self.brand = None # str
        
        #Lista que pode conter tanto o código EAN do produto (código de barras) quanto códigos ISBN (geralmente utilizados para livros)
        
        self.gtin = None # list[str]
        
        #Lista de categorias
        
        self.categories = None # list[str]
        
        # Lista de URLs de imagens. Pelo menos uma imagem precisa ser informada
        
        self.images = None # list[str]
        
        # Lista de URLs de vídeos
        
        self.videos = None # list[str]
        
        #Informações de preço do produto
        
        self.price = None # ProductLoadPrices
        
        #Informações de estoque do produto
        
        self.stock = None # ProductLoadStock
        
        #Informações de dimensões do produto
        
        self.dimensions = None # Dimensions
        
        #Informações de embrulho para presente
        
        self.gift_wrap = None # GiftWrap
        
        #Características do produto
        
        self.attributes = None # list[ProductAttribute]
        
        #Lista de erros que ocorreram na importação do produto
        
        self.errors = None # list[Error]
        
