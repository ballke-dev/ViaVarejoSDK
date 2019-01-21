#!/usr/bin/env python

import sys
import os

from ..model import *


class OrdersApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_orders(self, **kwargs):
        """Recupera detalhes de todos os pedidos
        <p>Operação utilizada para retornar informações de todos os pedidos, independente do status em que se encontram os mesmos.</p><p>Observação:<br/>Os campos retornados dependem do status do pedido, por exemplo, no status new, as informações de entrega são suprimidas para evitar a entrega antes da confirmação do pagamento. Nesta documentação estão presentes todos os campos de Pedido. Para saber quais campos são retornados para cada status do pedido, basta consultar a documentação de cada um dos métodos de consulta de pedidos por status.</p>

        Args:
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersResponse
        """

        allParams = ['_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders'
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

        responseObject = self.apiClient.deserialize(response, 'GetOrdersResponse')
        return responseObject
        
        
        
    
    def post_order(self, **kwargs):
        """Operação para criar um pedido
        <p>Operação que cria um pedido.</p><p class='obs obs-danger' >Esta operação só está disponível em ambiente de Sandbox para que seja possível executar todo o fluxo de testes da aplicação.</p><p class='obs'>É necessário aguardar cerca de 30 minutos para que o pedido seja indexado. Após esse período será possível consultar os pedidos através do serviço <a href='#!/orders/getOrdersByStatusNew_get_2' target='_blank'><strong>GET /orders/status/new</strong></a>. O Pedido só pode ser aprovado após aparecer com status <strong>NEW</strong>.<br/><br/>Clique <a href='../tutoriais/exemplo_orders_v2.json' target='_blank'>aqui</a> para obter um exemplo de conteúdo JSON suportado por esse serviço.</p><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para método POST, sendo retornado apenas o Status HTTP 201 - Created.</strong></p>

        Args:
            order, OrderSandbox: Objeto para criação do pedido. (required)
            

        Returns: str
        """

        allParams = ['order']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_order" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['order']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_orders_by_status_approved(self, **kwargs):
        """Recupera uma lista de pedidos Aprovados
        <p>Recupera uma lista de pedidos com status Aprovado que estão relacionados com o token do lojista informado. Este serviço irá retornar um ou mais pedidos que já possua pagamento aprovado, ou seja, são pedidos que podem ter o processo de entrega iniciado de imediato.</p><p class='obs obs-danger'>Obs.: Os emails transacionais que reportam o status do pedido para os clientes devem ser desabibilitados. Esse tipo de email já é enviado pelo Marketplace.</p>

        Args:
            approved_at, str: Data de aprovação. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>approvedAt={data inicial},{data final}</strong><br/><strong>approvedAt={data inicial},*</strong><br/><strong>approvedAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            customer_name, str: Nome do Cliente. (required)
            customer_document_number, str: Documento do Cliente. (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersResponse
        """

        allParams = ['approved_at', 'customer_name', 'customer_document_number', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_by_status_approved" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/approved'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('approved_at' in params):
            queryParams['approvedAt'] = self.apiClient.toPathValue(params['approved_at'])
        
        if ('customer_name' in params):
            queryParams['customer.name'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('customer_document_number' in params):
            queryParams['customer.documentNumber'] = self.apiClient.toPathValue(params['customer_document_number'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersResponse')
        return responseObject
        
        
        
    
    def put_seller_items_status_approved(self, **kwargs):
        """Operação para realizar a aprovação de um pedido (SANDBOX)
        <p class='obs obs-danger'>Essa operação está disponível apenas para SANDBOX.</p><p>Operação para realizar a aprovação de um pedido.</p><p class='obs'><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para métodos PUT e DELETE, sendo retornado apenas o Status HTTP 204 - No Content.</strong></p>

        Args:
            order_id, str: ID do pedido. (required)
            

        Returns: str
        """

        allParams = ['order_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_seller_items_status_approved" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/approved/{orderId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_orders_by_status_canceled(self, **kwargs):
        """Retorna uma lista de pedidos Cancelados
        <p>Retorna uma lista de pedidos Cancelados que estão relacionados com o token do lojista informado.</p><p class='obs obs-danger'>Obs.: Os emails transacionais que reportam o status do pedido para os clientes devem ser desabibilitados. Esse tipo de email já é enviado pelo Marketplace.</p>

        Args:
            canceled_at, str: Data de cancelemento. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>canceledAt={data inicial},{data final}</strong><br/><strong>canceledAt={data inicial},*</strong><br/><strong>canceledAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            customer_name, str: Nome do Cliente. (required)
            customer_document_number, str: Documento do Cliente. (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersResponse
        """

        allParams = ['canceled_at', 'customer_name', 'customer_document_number', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_by_status_canceled" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/canceled'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('canceled_at' in params):
            queryParams['canceledAt'] = self.apiClient.toPathValue(params['canceled_at'])
        
        if ('customer_name' in params):
            queryParams['customer.name'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('customer_document_number' in params):
            queryParams['customer.documentNumber'] = self.apiClient.toPathValue(params['customer_document_number'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersResponse')
        return responseObject
        
        
        
    
    def get_orders_by_status_delivered(self, **kwargs):
        """Recupera uma lista de pedidos Entregues
        <p>Recupera uma lista de pedidos Entregues que estão relacionados com o token do lojista informado. Este estado representa os pedidos cujos itens foram todos entregues.</p><p class='obs obs-danger'>Obs.: Os emails transacionais que reportam o status do pedido para os clientes devem ser desabibilitados. Esse tipo de email já é enviado pelo Marketplace.</p>

        Args:
            delivered_at, str: Data de entrega. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>deliveredAt={data inicial},{data final}</strong><br/><strong>deliveredAt={data inicial},*</strong><br/><strong>deliveredAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            customer_name, str: Nome do Cliente. (required)
            customer_document_number, str: Documento do Cliente. (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersResponse
        """

        allParams = ['delivered_at', 'customer_name', 'customer_document_number', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_by_status_delivered" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/delivered'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('delivered_at' in params):
            queryParams['deliveredAt'] = self.apiClient.toPathValue(params['delivered_at'])
        
        if ('customer_name' in params):
            queryParams['customer.name'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('customer_document_number' in params):
            queryParams['customer.documentNumber'] = self.apiClient.toPathValue(params['customer_document_number'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersResponse')
        return responseObject
        
        
        
    
    def get_orders_by_status_new(self, **kwargs):
        """Recupera uma lista de pedidos Novos
        <p>Recupera uma lista de pedidos com status Novo que estão relacionados com o token do lojista informado. Este estado representa os pedidos fechados que ainda não foram aprovados, ou seja, pedidos que ainda não devem ser entregues, pois estão aguardado o pagamento. Alguns campos não serão enviados, para evitar a entrega antes da confirmação do pagamento.</p><p class='obs obs-danger'>Obs.: Os emails transacionais que reportam o status do pedido para os clientes devem ser desabibilitados. Esse tipo de email já é enviado pelo Marketplace.</p>

        Args:
            purchased_at, str: Data de compra. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>purchasedAt={data inicial},{data final}</strong><br/><strong>purchasedAt={data inicial},*</strong><br/><strong>purchasedAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            customer_name, str: Nome do Cliente. (required)
            customer_document_number, str: Documento do Cliente. (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersStatusNewResponse
        """

        allParams = ['purchased_at', 'customer_name', 'customer_document_number', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_by_status_new" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/new'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('purchased_at' in params):
            queryParams['purchasedAt'] = self.apiClient.toPathValue(params['purchased_at'])
        
        if ('customer_name' in params):
            queryParams['customer.name'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('customer_document_number' in params):
            queryParams['customer.documentNumber'] = self.apiClient.toPathValue(params['customer_document_number'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersStatusNewResponse')
        return responseObject
        
        
        
    
    def get_orders_by_status_partially_delivered(self, **kwargs):
        """Retorna uma lista de pedidos Parcialmente Entregues
        <p>Retorna uma lista de pedidos Parcialmente Entregues que estão relacionados com o token do lojista informado.</p><p class='obs'> Os pedidos ficam nesse estado apenas quando ocorreu quebra de entrega e alguns produtos da lista completa já foram sinalizados como Entregues pelo serviço <a href='#!/orders/persistTracking_post_10' target='_blank'><strong>POST /orders/{orderId}/trackings/delivered</strong></a></p><p class='obs obs-danger'>Obs.: Os emails transacionais que reportam o status do pedido para os clientes devem ser desabibilitados. Esse tipo de email já é enviado pelo Marketplace.</p>

        Args:
            sent_at, str: Data de envio. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>sentAt={data inicial},{data final}</strong><br/><strong>sentAt={data inicial},*</strong><br/><strong>sentAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            customer_name, str: Nome do Cliente. (required)
            customer_document_number, str: Documento do Cliente. (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersResponse
        """

        allParams = ['sent_at', 'customer_name', 'customer_document_number', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_by_status_partially_delivered" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/partiallyDelivered'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('sent_at' in params):
            queryParams['sentAt'] = self.apiClient.toPathValue(params['sent_at'])
        
        if ('customer_name' in params):
            queryParams['customer.name'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('customer_document_number' in params):
            queryParams['customer.documentNumber'] = self.apiClient.toPathValue(params['customer_document_number'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersResponse')
        return responseObject
        
        
        
    
    def get_orders_by_status_partially_sent(self, **kwargs):
        """Retorna uma lista de pedidos Parcialmente Enviados
        <p>Retorna uma lista de pedidos Parcialmente Enviados que estão relacionados com o token do lojista informado. Ocorre quando um ou mais itens foram enviados, porém ainda existem itens que não foram enviados.</p><p class='obs'> Os pedidos ficam nesse estado apenas quando ocorreu quebra de entrega e alguns produtos da lista completa já foram sinalizados como Enviados pelo serviço <a href='#!/orders/persistTracking_post_9' target='_blank'><strong>POST /orders/{orderId}/trackings/sent</strong></a></p><p class='obs obs-danger'>Obs.: Os emails transacionais que reportam o status do pedido para os clientes devem ser desabibilitados. Esse tipo de email já é enviado pelo Marketplace.</p>

        Args:
            sent_at, str: Data de envio. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>sentAt={data inicial},{data final}</strong><br/><strong>sentAt={data inicial},*</strong><br/><strong>sentAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas. (required)
            customer_name, str: Nome do Cliente. (required)
            customer_document_number, str: Documento do Cliente. (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetOrdersResponse
        """

        allParams = ['sent_at', 'customer_name', 'customer_document_number', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_by_status_partially_sent" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/partiallySent'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('sent_at' in params):
            queryParams['sentAt'] = self.apiClient.toPathValue(params['sent_at'])
        
        if ('customer_name' in params):
            queryParams['customer.name'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('customer_document_number' in params):
            queryParams['customer.documentNumber'] = self.apiClient.toPathValue(params['customer_document_number'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersResponse')
        return responseObject
        
        
        
    
    def get_orders_by_status_sent(self, **kwargs):
        """Recupera uma lista de pedidos Enviados
        <p>Recupera uma lista de pedidos com status Enviado, que estão relacionados com o token do lojista informado. Este estado representa os pedidos cujos itens foram todos entregues.</p><p class='obs obs-danger'>Obs.: Os emails transacionais que reportam o status do pedido para os clientes devem ser desabibilitados. Esse tipo de email já é enviado pelo Marketplace.</p>

        Args:
            sent_at, str: Data de envio. Esse campo aceita um range de datas separados por vírgula, e os formatos aceitos para o campo são os seguintes:<br/><strong>sentAt={data inicial},{data final}</strong><br/><strong>sentAt={data inicial},*</strong><br/><strong>sentAt=*,{data final}</strong><br/>onde, o <strong>*</strong> é obrigatório e indica a que todas as datas antes ou depois da outra data passada devem ser consideradas (required)
            customer_name, str: Nome do Cliente (required)
            customer_document_number, str: Documento do Cliente (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial da consulta. O registro inicial tem índice zero (0), ou seja, para trazer os 10 primeiros registros, informa 0 para _offset e 10 para _limit. (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta (required)
            

        Returns: GetOrdersResponse
        """

        allParams = ['sent_at', 'customer_name', 'customer_document_number', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_orders_by_status_sent" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/status/sent'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('sent_at' in params):
            queryParams['sentAt'] = self.apiClient.toPathValue(params['sent_at'])
        
        if ('customer_name' in params):
            queryParams['customer.name'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('customer_document_number' in params):
            queryParams['customer.documentNumber'] = self.apiClient.toPathValue(params['customer_document_number'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetOrdersResponse')
        return responseObject
        
        
        
    
    def get_order_by_id(self, **kwargs):
        """Recupera detalhes do pedido informado
        <p>Recupera detalhes do pedido informado.</p><p>Observação:<br/>Os campos retornados dependem do status do pedido, por exemplo, no status new, as informações de entrega são suprimidas para evitar a entrega antes da confirmação do pagamento. Nesta documentação estão presentes todos os campos de Pedido. Para saber quais campos são retornados para cada status do pedido, basta consultar a documentação de cada um dos métodos de consulta de pedidos por status.</p><p class='obs'>Deve ser informado um pedido válido.</p><p class='obs obs-danger'>Abaixo seguem os valores possíveis para o tipo de pagamento (paymentType)<table class='table'><tr><th>Código</th><th>Descrição</th></tr><tr><td>1</td><td>Cartão de Crédito</td></tr><tr><td>2</td><td>Boleto</td></tr><tr><td>4</td><td>Cupom</td></tr><tr><td>5</td><td>Transferência</td></tr></table></p><p class='obs obs-danger'>Segue abaixo a lista de Status existentes para pedidos. Os status representam a situação consolidada do pedido:<br/><table class = 'table'><tr><th>Código</th><th>Descrição</th></tr><tr><td>NEW</td><td>Novo</td></tr><tr><td>GDE</td><td>Entregas geradas</td></tr><tr><td>PEN</td><td>Pagamento pendente</td></tr><tr><td>PAY</td><td>Pagamento aprovado</td></tr><tr><td>SHP</td><td>Enviado</td></tr><tr><td>DLV</td><td>Entregue</td></tr></table></p><p class='obs obs-danger'>Segue abaixo a lista de Control Points existentes. Os Control Points estão presentes em cada operação de tracking e representam o status de cada operação realizada no pedido:<br/><table class = 'table'><tr><th>Código</th><th>Sequência / ordem</th><th>Descrição</th></tr><tr><td>AAP</td><td>1</td><td>Aguardando a confirmação do pagamento</td></tr><tr><td>ACR</td><td>2</td><td>Análise de dados</td></tr><tr><td>ADT</td><td>3</td><td>Data de entrega ajustada</td></tr><tr><td>AEG</td><td>4</td><td>Aguardando entregas pagamento</td></tr><tr><td>AES</td><td>5</td><td>Disponibilidade de estoque</td></tr><tr><td>AGR</td><td>6</td><td>Dificuldade na entrega</td></tr><tr><td>AMC</td><td>7</td><td>Análise de dados</td></tr><tr><td>AR1</td><td>8</td><td>Aviso de Entrega 1</td></tr><tr><td>AR2</td><td>9</td><td>Aviso de Entrega 2</td></tr><tr><td>ARE</td><td>10</td><td>Aguardando Retirada</td></tr><tr><td>ARL</td><td>11</td><td>Disponível para Entrega</td></tr><tr><td>ATR</td><td>12</td><td>Dificuldade na entrega</td></tr><tr><td>AU1</td><td>13</td><td>Dificuldade na entrega</td></tr><tr><td>AU2</td><td>14</td><td>Dificuldade na entrega</td></tr><tr><td>AU3</td><td>15</td><td>Dificuldade na entrega</td></tr><tr><td>AVA</td><td>16</td><td>Dificuldade na entrega</td></tr><tr><td>CAN</td><td>17</td><td>Entrega Cancelada</td></tr><tr><td>CAP</td><td>18</td><td>Análise de dados concluída</td></tr><tr><td>DAE</td><td>19</td><td>Data de Entrega Ajustada</td></tr><tr><td>DIV</td><td>20</td><td>Dificuldade na entrega</td></tr><tr><td>DNE</td><td>21</td><td>Dificuldade na entrega</td></tr><tr><td>EA1</td><td>22</td><td>Destinatário Ausente - 1ª tentativa</td></tr><tr><td>EAR</td><td>23</td><td>Entrega em andamento</td></tr><tr><td>END</td><td>24</td><td>Dificuldade na entrega</td></tr><tr><td>ENL</td><td>25</td><td>Endereço não localizado</td></tr><tr><td>ENT</td><td>26</td><td>Entrega concluída</td></tr><tr><td>EPR</td><td>27</td><td>Entrega em andamento</td></tr><tr><td>ETR</td><td>28</td><td>Entrega em andamento</td></tr><tr><td>EXT</td><td>29</td><td>Dificuldade na entrega</td></tr><tr><td>FEL</td><td>30</td><td>Entrega em andamento</td></tr><tr><td>FIS</td><td>31</td><td>Dificuldade na entrega</td></tr><tr><td>IED</td><td>32</td><td>Dificuldade na entrega</td></tr><tr><td>INS</td><td>33</td><td>Produto instalado</td></tr><tr><td>LIF</td><td>34</td><td>Entrega em andamento</td></tr><tr><td>MDS</td><td>35</td><td>Dificuldade na entrega</td></tr><tr><td>MPA</td><td>36</td><td>Aguardando a confirmação do pagamento</td></tr><tr><td>NFS</td><td>37</td><td>Nota Fiscal emitida</td></tr><tr><td>OCO</td><td>38</td><td>Entrega concluída</td></tr><tr><td>PAP</td><td>39</td><td>Pagamento aprovado</td></tr><tr><td>PEI</td><td>40</td><td>Pedido incluso</td></tr><tr><td>PNA</td><td>41</td><td>Pagamento não aprovado</td></tr><tr><td>PRE</td><td>42</td><td>Pedido recusado pelo Cliente</td></tr><tr><td>REC</td><td>43</td><td>Análise de dados não confirmada</td></tr><tr><td>RED</td><td>44</td><td>Entrega em andamento</td></tr><tr><td>REO</td><td>45</td><td>Dificuldade na entrega</td></tr><tr><td>REV</td><td>46</td><td>Pagamento não aprovado</td></tr><tr><td>RIE</td><td>47</td><td>Impossibilidade de entrega do produto</td></tr><tr><td>ROT</td><td>48</td><td>Entrega em andamento</td></tr><tr><td>ROU</td><td>49</td><td>Dificuldade na entrega</td></tr><tr><td>RTD</td><td>50</td><td>Em rota de devolução</td></tr><tr><td>VES</td><td>51</td><td>Disponibilidade de estoque</td></tr><tr><td>WMS</td><td>52</td><td>Separação e embalagem</td></tr></table></p>

        Args:
            order_id, str: ID do pedido. (required)
            

        Returns: Order
        """

        allParams = ['order_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_order_by_id" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/{orderId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Order')
        return responseObject
        
        
        
    
    def get_order_by_id_and_sku_sller_id(self, **kwargs):
        """Recupera detalhes de um item específico do pedido
        <p>Recupera detalhes de um item específico do pedido.</p><p class='obs'>Deve ser informado um pedido e um item do pedido válidos.</p>

        Args:
            order_id, str: ID do pedido. (required)
            sku_seller_id, str: SKU Seller ID do item de pedido. (required)
            

        Returns: OrderItem
        """

        allParams = ['order_id', 'sku_seller_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_order_by_id_and_sku_sller_id" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/{orderId}/items/{skuSellerId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        
        if ('sku_seller_id' in params):
            replacement = str(self.apiClient.toPathValue(params['sku_seller_id']))
            resourcePath = resourcePath.replace('{' + 'skuSellerId' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'OrderItem')
        return responseObject
        
        
        
    
    def post_order_tracking_cancelation(self, **kwargs):
        """Operação para confirmar o cancelamento de um item de pedido
        <p>Operação utilizada para confirmar o cancelamento de um item de pedido que foi aberto pelo cliente (via protocolo) ou cancelamento acionado pelo lojista.</p><p class='obs'><strong>Quebra de envio</strong><br/>No caso de quebra de envio, passe apenas os itens e a quantidade que serão enviados.<br/>O controle de quais itens foram enviados deverá ser realizado pela sua Aplicação.<br/><br/>Para notificar o envio de todos os produtos, passe a lista contendo todos os itens e quantidade total.<br/><br/>Clique <a href='../tutoriais/exemplo_tracking_sent_v2.json' target='_blank'>aqui</a> para obter um exemplo de conteúdo JSON suportado por esse serviço.</p><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para método POST, sendo retornado apenas o Status HTTP 201 - Created.</strong></p>

        Args:
            body, NewTracking:  (required)
            order_id, str: ID do pedido. (required)
            

        Returns: str
        """

        allParams = ['body', 'order_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_order_tracking_cancelation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/{orderId}/trackings/cancel'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def post_order_tracking_delivered(self, **kwargs):
        """Registra uma nova operação de tracking de entrega
        <p>Registra uma nova operação de tracking de Entrega para os itens do pedido.</p><p class='obs'><strong>Quebra de envio</strong><br/>No caso de quebra de envio, passe apenas os itens e a quantidade que foram entregues.<br/>O controle de quais itens foram enviados deverá ser realizado pela sua Aplicação.<br/><br/>Para notificar a entrega de todos os produtos, passe a lista contendo todos os itens e quantidade total.<br/><br/>Clique <a href='../tutoriais/exemplo_tracking_delivered_v2.json' target='_blank'>aqui</a> para obter um exemplo de conteúdo JSON suportado por esse serviço.</p><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para método POST, sendo retornado apenas o Status HTTP 201 - Created.</strong></p>

        Args:
            body, NewTracking:  (required)
            order_id, str: ID do pedido. (required)
            

        Returns: str
        """

        allParams = ['body', 'order_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_order_tracking_delivered" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/{orderId}/trackings/delivered'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def post_order_tracking_exchange(self, **kwargs):
        """Operação para confirmar a troca de um item de um pedido
        <p>Operação utilizada para confirmar a troca de um item de pedido aberto pelo cliente (via protocolo).</p><p class='obs'><strong>Quebra de envio</strong><br/>No caso de quebra de envio, passe apenas os itens e a quantidade que serão enviados.<br/>O controle de quais itens foram enviados deverá ser realizado pela sua Aplicação.<br/><br/>Para notificar o envio de todos os produtos, passe a lista contendo todos os itens e quantidade total.<br/><br/>Clique <a href='../tutoriais/exemplo_tracking_sent_v2.json' target='_blank'>aqui</a> para obter um exemplo de conteúdo JSON suportado por esse serviço.</p><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para método POST, sendo retornado apenas o Status HTTP 201 - Created.</strong></p>

        Args:
            body, NewTracking:  (required)
            order_id, str: ID do pedido. (required)
            

        Returns: str
        """

        allParams = ['body', 'order_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_order_tracking_exchange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/{orderId}/trackings/exchange'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def post_order_tracking_return(self, **kwargs):
        """Operação para confirmar devolução (reembolso) de item do pedido
        <p>Operação utilizada para confirmação de devolução (reembolso) de item do pedido através de protocolo aberto pelo cliente.</p><p class='obs'><strong>Quebra de envio</strong><br/>No caso de quebra de envio, passe apenas os itens e a quantidade que serão enviados.<br/>O controle de quais itens foram enviados deverá ser realizado pela sua Aplicação.<br/><br/>Para notificar o envio de todos os produtos, passe a lista contendo todos os itens e quantidade total.<br/><br/>Clique <a href='../tutoriais/exemplo_tracking_sent_v2.json' target='_blank'>aqui</a> para obter um exemplo de conteúdo JSON suportado por esse serviço.</p><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para método POST, sendo retornado apenas o Status HTTP 201 - Created.</strong></p>

        Args:
            body, NewTracking:  (required)
            order_id, str: ID do pedido. (required)
            

        Returns: str
        """

        allParams = ['body', 'order_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_order_tracking_return" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/{orderId}/trackings/return'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def post_order_tracking_sent(self, **kwargs):
        """Registra uma nova operação de tracking de envio
        <p>Registra uma nova operação de tracking de Envio para os itens do pedido.</p><p class='obs'><strong>Quebra de envio</strong><br/>No caso de quebra de envio, passe apenas os itens e a quantidade que serão enviados.<br/>O controle de quais itens foram enviados deverá ser realizado pela sua Aplicação.<br/><br/>Para notificar o envio de todos os produtos, passe a lista contendo todos os itens e quantidade total.<br/><br/>Clique <a href='../tutoriais/exemplo_tracking_sent_v2.json' target='_blank'>aqui</a> para obter um exemplo de conteúdo JSON suportado por esse serviço.</p><strong>Retorno do Serviço</strong><br/>O retorno deste serviço é baseado no padrão definido para método POST, sendo retornado apenas o Status HTTP 201 - Created.</strong></p>

        Args:
            body, NewTracking:  (required)
            order_id, str: ID do pedido. (required)
            

        Returns: str
        """

        allParams = ['body', 'order_id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_order_tracking_sent" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/orders/{orderId}/trackings/sent'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('order_id' in params):
            replacement = str(self.apiClient.toPathValue(params['order_id']))
            resourcePath = resourcePath.replace('{' + 'orderId' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    


