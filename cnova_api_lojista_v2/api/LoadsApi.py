#!/usr/bin/env python

import sys
import os

from ..model import *


class LoadsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_orders_tracking_delivered(self, **kwargs):
        """Operação utilizada para consultar o status dos produtos enviados
        <p>Operação utilizada para consultar o status de uma lista de produtos enviados. É possível refinar a consulta utilizando alguns parâmetros não obrigatórios como: STATUS e DATA DE CADASTRO DO PRODUTO</p>

        Args:
            created_at, str: Data de envio do produto. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>purchasedAt={data inicial},{data final}</strong><br/><strong>purchasedAt={data inicial},*</strong><br/><strong>purchasedAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            status, str: Status do produto importado. (required)
            _offset, int: Parâmetro utilizado para indicar a posição do registro inicial que será trazido. A primeira posição é sempre zero (0) (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta (required)
            

        Returns: GetOrdersTrackingUpdatingResponse
        """

        allParams = ['created_at', 'status', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_tracking_delivered" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/orders/trackings/delivered'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('created_at' in params):
            queryParams['createdAt'] = self.apiClient.toPathValue(params['created_at'])
        
        if ('status' in params):
            queryParams['status'] = self.apiClient.toPathValue(params['status'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersTrackingUpdatingResponse')
        return responseObject
        
        
        
    
    def post_orders_tracking_delivered(self, **kwargs):
        """Operação utilizada  para atualização de tracking massivo
        <p>Operação utilizada para atualização de tracking massivo. </p><br/><p class='obs obs-danger'>Devido ao formato JSON, é necessário alterar o <strong>HTTP Header: content-type</strong> para <strong>application/json</strong> para o correto funcionamento. <p class='obs'><strong>Retorno do Serviço</strong><br />O retorno deste serviço é baseado no padrão definido para métodos POST segundo o Status HTTP 201 - Created.</p>

        Args:
            orders_trackings, OrdersTrackings: Arquivo em formato <strong>JSON</strong> cujo conteúdo contêm uma lista de objetos product. (required)
            

        Returns: str
        """

        allParams = ['orders_trackings']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_orders_tracking_delivered" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/orders/trackings/delivered'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['orders_trackings']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_orders_tracking_sent(self, **kwargs):
        """Operação utilizada para consultar o status dos produtos enviados
        <p>Operação utilizada para consultar o status de uma lista de produtos enviados. É possível refinar a consulta utilizando alguns parâmetros não obrigatórios como: STATUS e DATA DE CADASTRO DO PRODUTO.</p>

        Args:
            created_at, str: Data de envio do produto. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>purchasedAt={data inicial},{data final}</strong><br/><strong>purchasedAt={data inicial},*</strong><br/><strong>purchasedAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            status, str: Status do produto importado. (required)
            _offset, int: Parâmetro utilizado para indicar a posição do registro inicial que será trazido. A primeira posição é sempre zero (0). (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersTrackingUpdatingResponse
        """

        allParams = ['created_at', 'status', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_tracking_sent" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/orders/trackings/sent'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('created_at' in params):
            queryParams['createdAt'] = self.apiClient.toPathValue(params['created_at'])
        
        if ('status' in params):
            queryParams['status'] = self.apiClient.toPathValue(params['status'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersTrackingUpdatingResponse')
        return responseObject
        
        
        
    
    def post_orders_tracking_sent(self, **kwargs):
        """Operação utilizada para atualização de tracking massivo
        <p>Operação utilizada para atualização de tracking massivo. </p><br/><p class='obs obs-danger'> Devido ao formato JSON, é necessário alterar o <strong>HTTP Header: content-type</strong> para <strong>application/json</strong> para o correto funcionamento. <p class='obs'><strong>Retorno do Serviço</strong><br />O retorno deste serviço é baseado no padrão definido para métodos POST segundo o Status HTTP 201 - Created.</p>

        Args:
            orders_trackings, OrdersTrackings: Arquivo em formato <strong>JSON</strong> cujo conteúdo contêm uma lista de objetos de order tracking. (required)
            

        Returns: str
        """

        allParams = ['orders_trackings']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_orders_tracking_sent" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/orders/trackings/sent'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['orders_trackings']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_products(self, **kwargs):
        """Operação utilizada para consultar o status dos produtos
        <p>Operação utilizada para consultar o status de uma lista de produtos enviados. É possível refinar a consulta utilizando alguns parâmetros não obrigatórios como: STATUS e DATA DE CADASTRO DO PRODUTO.</p>

        Args:
            created_at, str: Data de envio do produto. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>purchasedAt={data inicial},{data final}</strong><br/><strong>purchasedAt={data inicial},*</strong><br/><strong>purchasedAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            status, str: Status do produto importado. (required)
            _offset, int: Parâmetro utilizado para indicar a posição do registro inicial que será trazido. A primeira posição é sempre zero (0). (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetProductsResponse
        """

        allParams = ['created_at', 'status', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_products" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/products'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('created_at' in params):
            queryParams['createdAt'] = self.apiClient.toPathValue(params['created_at'])
        
        if ('status' in params):
            queryParams['status'] = self.apiClient.toPathValue(params['status'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetProductsResponse')
        return responseObject
        
        
        
    
    def post_products(self, **kwargs):
        """Operação utilizada para enviar uma nova carga de produtos (assíncrono)
        <p class='obs obs-danger'>Não é possível executar testes com esta operação via API Browser devido ao envio de arquivos, não suportado pela ferramenta.</p><p>Operação utilizada para envio de carga contendo novos produtos. Através desta é possível passar, de forma não obrigatória, informações da ficha dos produtos e informações de venda, tais como valor e quantidade.</p><p class='obs'>Não é objetivo deste serviço o recebimento de informações para atualização de preço e estoque (para isso utilize os serviços existentes no recurso <a href='#!/sellerItems' target='_blank'><strong>/sellerItems</strong></a>), nem a atualização da ficha cadastral do produto (não há serviço disponível para essa finalidade, se precisar atualizar a ficha do produto, entre em contato com o time Comercial do Marketplace).<br/><br/><strong>IMPORTANTE</strong><br/>Caso sua Loja já tenha produtos no Marketplace que não foram enviados através da API (enviados via planilha excel, por exemplo), não os envie novamente em uma nova carga, faça primeiro a consulta de seus produtos através do serviço <a href='#!/sellerItems/getSellerItems_get_0' target='_blank'><strong>GET /sellerItems</strong></a> e realize o DE-PARA de skus.</p><p class='obs obs-danger'> Devido ao formato JSON, é necessário alterar o <strong>HTTP Header: content-type</strong> para <strong>application/json</strong> para o correto funcionamento.<br /> <br />Clique <a href='../tutoriais/exemplo_loads_v2.json' target='_blank'>aqui</a> para obter um exemplo de conteúdo JSON suportado por essa operação.</p><p class='obs'> <strong>Categorias e atributos</strong><br /><br /> <strong>SANDBOX</strong><br /><br/>Para os testes na SANDBOX é obrigatório passar uma categoria fixa chamada <strong>'Teste>API'</strong>. Caso seja enviada qualquer outra categoria, o produto ficará no status <strong>Pending</strong> e, em Sandbox, não há tratamento para esse tipo de status. Se isso acontecer, cancele o seu produto com a operação exlusiva de Sandbox <a href='#!/loads/deleteProducts_delete_2' target='_blank'><strong>DELETE /loads/products/{skuSellerId}</strong></a><br /><br /> <strong>PRODUÇÃO</strong><br/><br/>Em produção, envie a categoria real do produto do lojista, não é necessário fazer o DE-PARA para a árvore de categorias do Marketplace.<br /> Lembre-se apenas de seguir a seguinte regra:<br /> <strong>'Informática>Notebook'</strong>, onde Informática é a categoria pai e Notebook é a subcategoria e elas devem ser separadas pelo sinal de maior <strong>'>'</strong>.<br />Cada categoria da árvore de produtos da Cnova possui um conjunto de atributos opcionais e obrigatórios. Para saber quais são os atributos obrigatórios para a categoria de produtos que serão carregados, por favor consulte o seu contato comercial ou abra uma solicitação através de <a href='http://suporte-lojistas.extra.com.br'>Suporte-lojistas.</a> É sempre recomendável o envio do máximo de atributos disponíveis na base de origem para maximizar a qualidade das fichas de produto e os resultados de busca do produto.<br/> </p><p class='obs obs-danger'> <strong>Sobre o processo de importação</strong> <br /><br/>Esta operação é assíncrona, ou seja, os produtos passam por um processamento em nosso sistema para depois ficarem disponíveis para consulta. Para consultar o status dos produtos enviados, utilize o serviço:<br/><a href='#!/loads/getLoadInfo_get_1' target='_blank'><strong>GET /loads/products</strong></a>.<br/>Caso existam erros, também é possível verificar quais foram os erros para cada produto enviado através do serviço:<br/><a href='#!/loads/getLoadInfoSkuOrigin_get_3' target='_blank'><strong>GET /loads/products/{skuSellerId}</strong></a><br /> Todos os produtos passam por um processo de aprovação antes da efetiva liberação no Marketplace. Atente-se para o processo de importação de produtos, que é diferente para cada ambiente:<br /><br/> <strong>SANDBOX</strong><br /><br/> Em Sandbox o processo de aprovação é automático, ou seja, uma vez que as cargas forem enviadas, se os produtos estiverem com a ficha cadastral correta, todos eles serão aprovados (assumirão o status Disponível - AVAILABLE).<br />Os produtos que forem aprovados automaticamente só estarão disponíveis na consulta de produtos do lojista (<a href='#!/sellerItems/getSellerItems_get_0' target='_blank'><strong>GET /sellerItems</strong></a>) após assumirem o status <strong>AVAILABLE.</strong><br/><br/> <strong>PRODUÇÃO</strong><br /><br/>Em Produção, antes que os produtos de uma carga sejam efetivamente cadastrados, eles passam por uma validação que fica sob a responsabilidade da Equipe de Cadastro do Marketplace e, por esse motivo, os produtos levam mais tempo para serem ativados no site ao qual você está apto a vender. Isso quer dizer que o produto não irá aparecer no site e nem estará disponível para atualizações de preço/estoque logo que enviado via carga. Consulte a equipe Comercial do Marketplace para informações sobre o prazo médio de cadastro dos produtos.</p><p class='obs obs-danger'><strong>Agrupamento de cargas</strong><br/><br/>Quando uma carga de produtos é enviada, caso, antes da aprovação dos produtos enviado, uma segunda carga seja enviada, e se um produto for enviado nas duas cargas, o que irá valer é o segundo produto enviado, ou seja, se na primeira carga você constatou que o produto estava com algum erro, é possível reenviá-lo com as correções para que ele seja considerado para importação.<br/>Enquanto o novo produto não for aprovado, é possível enviá-lo novamente para atualização da fichal cadastral. <strong>Mas lembre-se:</strong> para produtos já disponibilizados no Marketplace, esse serviço não realiza atualização da ficha cadastral, conforme mencionado acima.<br/>Outra forma de fazer essa correção unitária de um produto com problema é através do serviço <a href='#!/loads/getLoadInfoSkuOrigin_put_4' target='_blank'><strong>PUT /loads/products/{skuSellerId}</strong></a></p><p class='obs'><strong>Retorno do Serviço</strong><br />O retorno deste serviço é baseado no padrão definido para métodos POST segundo o Status HTTP 201 - Created.</p>

        Args:
            products, list[Product]: Arquivo em formato <strong>JSON</strong> cujo conteúdo contêm uma lista de objetos product. (required)
            

        Returns: str
        """

        allParams = ['products']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_products" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/products'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['products']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_product(self, **kwargs):
        """Operação para consultar um produto enviado
        <p>Operação para consultar um produto enviado.</p><p class='obs obs-danger'>Essa operação deve ser utilizada, principalmente, para recuperar a listagem de erros que podem ter ocorrido na importação de produtos. Não utilize esse serviço para recuperar os dados atuais do produto que está sendo vendido (como preço e estoque). Para recuperar informações de venda do produto, utilize o serviço <a href='#!/sellerItems/getDetailsSellerItemOrigin_get_1' target='_blank'><strong>GET /sellerItems/{skuSellerId}</strong></a></p>

        Args:
            sku_seller_id, str: SKU ID do Lojista. (required)
            

        Returns: GetProductWithErrorsResponse
        """

        allParams = ['sku_seller_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_product" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/products/{skuSellerId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetProductWithErrorsResponse')
        return responseObject
        
        
        
    
    def put_product(self, **kwargs):
        """Operação para alterar um produto enviado na carga
        <p>Operação utilizada para alterar um produto enviado na carga.</p><p class='obs obs-danger'>O produto só pode ser alterado antes de assumir o status Disponível (AVAILABLE).<br/>Produtos já disponíveis não podem ser alterados através de serviços. Para mais informações, leia a documentação <a href='#!/loads/loadProducts_post_0' target='_blank'><strong>POST /loads/products</strong></a>.</p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            sku_seller_id, str: SKU do produto do lojista que deverá ser alterado. (required)
            body, Product: Parâmetros para alterar um produto enviado na carga. (required)
            

        Returns: str
        """

        allParams = ['sku_seller_id', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_product" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/products/{skuSellerId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def delete_product(self, **kwargs):
        """Operação utilizada para cancelar uma lista de produtos enviados (SANDBOX)
        <p class='obs obs-danger'>Essa operação está disponível apenas para SANDBOX.</p><p>Operação utilizada para cancelar itens de uma carga. Os itens só podem ser cancelados se estiverem com erros de importação ou se os produtos estiverem pendentes (status=PENDING).</p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            sku_seller_id, str: SKU do produto do lojista que deverá ser alterado. (required)
            

        Returns: Errors
        """

        allParams = ['sku_seller_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete_product" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/products/{skuSellerId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Errors')
        return responseObject
        
        
        
    
    def get_seller_items_prices_updating_status(self, **kwargs):
        """Operação para consulta de atualização massiva de preços
        <p>Operação para consulta de status da atualização massiva de preços de produtos enviados.</p><p class='obs obs-danger'>Essa operação deve ser utilizada, principalmente, para recuperar a listagem de erros que podem ter ocorrido na importação de produtos. Não utilize esse serviço para recuperar os dados atuais do produto que está sendo vendido (como preço e estoque). Para recuperar informações de venda do produto, utilize o serviço <a href='#!/sellerItems/getDetailsSellerItemOrigin_get_1' target='_blank'><strong>GET /sellerItems/{skuSellerId}</strong></a></p>

        Args:
            _offset, int: Parâmetro utilizado para indicar a posição do registro inicial que será trazido. A primeira posição é sempre zero (0). (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetSellerItemsPricesUpdatingResponse
        """

        allParams = ['_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_seller_items_prices_updating_status" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/sellerItems/prices'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSellerItemsPricesUpdatingResponse')
        return responseObject
        
        
        
    
    def put_seller_items_prices(self, **kwargs):
        """Operação para atualização de preço de produtos em massa
        <p>Operação utilizada para atualização de preço, de forma massiva, de produtos enviados na carga.</p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            body, list[SellerItemPrices]: Parâmetros para ativação/desativação massiva de produtos (required)
            

        Returns: str
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_seller_items_prices" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/sellerItems/prices'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_seller_items_status_updating_status(self, **kwargs):
        """Operação para consulta da atualização massiva de status
        <p>Operação para consulta da atualização massiva de status de produtos enviado.</p><p class='obs obs-danger'>Essa operação deve ser utilizada, principalmente, para recuperar a listagem de erros que podem ter ocorrido na importação de produtos. Não utilize esse serviço para recuperar os dados atuais do produto que está sendo vendido (como preço e estoque). Para recuperar informações de venda do produto, utilize o serviço <a href='#!/sellerItems/getDetailsSellerItemOrigin_get_1' target='_blank'><strong>GET /sellerItems/{skuSellerId}</strong></a></p>

        Args:
            _offset, int: Parâmetro utilizado para indicar a posição do registro inicial que será trazido. A primeira posição é sempre zero (0). (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetSellerItemsStatusUpdatingResponse
        """

        allParams = ['_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_seller_items_status_updating_status" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/sellerItems/status'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSellerItemsStatusUpdatingResponse')
        return responseObject
        
        
        
    
    def put_seller_items_status(self, **kwargs):
        """Operação para ativação/desativação massiva de produtos
        <p>Operação utilizada para ativação/desativação massiva de produtos enviados na carga.</p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            body, list[SellerItemStatusUpdate]: Parâmetros para ativação/desativação massiva de produtos (required)
            

        Returns: str
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_seller_items_status" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/sellerItems/status'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_seller_items_stocks_updating_status(self, **kwargs):
        """Operação para consulta do status da atualização massiva de estoque
        <p>Operação para consulta do status da atualização massiva de estoque de produtos enviados.</p><p class='obs obs-danger'>Essa operação deve ser utilizada, principalmente, para recuperar a listagem de erros que podem ter ocorrido na importação de produtos. Não utilize esse serviço para recuperar os dados atuais do produto que está sendo vendido (como preço e estoque). Para recuperar informações de venda do produto, utilize o serviço <a href='#!/sellerItems/getDetailsSellerItemOrigin_get_1' target='_blank'><strong>GET /sellerItems/{skuSellerId}</strong></a></p>

        Args:
            _offset, int: Parâmetro utilizado para indicar a posição do registro inicial que será trazido. A primeira posição é sempre zero (0). (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetSellerItemsStocksUpdatingResponse
        """

        allParams = ['_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_seller_items_stocks_updating_status" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/sellerItems/stocks'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSellerItemsStocksUpdatingResponse')
        return responseObject
        
        
        
    
    def put_seller_items_stocks(self, **kwargs):
        """Operação para atualização de estoque de produtos em massa
        <p>Operação utilizada para atualização de estoque, de forma massiva, de produtos enviados na carga.</p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            body, list[SellerItemStocks]: Parâmetros para atualização massiva de estoque de produtos. (required)
            

        Returns: str
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_seller_items_stocks" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/loads/sellerItems/stocks'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    


