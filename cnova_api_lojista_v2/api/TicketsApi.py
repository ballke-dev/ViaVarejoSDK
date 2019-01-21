#!/usr/bin/env python

import sys
import os

from ..model import *


class TicketsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def get_tickets(self, **kwargs):
        """Operação utilizada para consultar os protocolos
        <p>Esse serviço permite que as plataformas consigam integrar suas ferramentas de atendimento com o processo de atendimento/pós vendas do Marketplace. Um Ticket representa um atendimento feito ao consumidor final. São diversas possibilidades de atendimento ao consumidor, o consumidor pode iniciar o atendimento através dá página de contato do site do <a href=http://atendimento.extra.com.br/viewclient/faces/pages/contact.xhtml><strong>Extra</strong></a> .</p>

        Args:
            status, str: Utilizado para filtrar os tickets com um status específico. Aberto (opened), Em Monitoramento (attendance), Fechado (closed). (required)
            code, str: Código do protocolo. (required)
            customer_name, str: Nome do comprador (ou parte dele). (required)
            created_at, str: Utilizado para filtrar tickets pela data de criação. É possível passar uma variação de datas separadas por ','. Ex: 2014-12-15T11:00:00.000-02:00,*. (required)
            closed_at, str: Utilizado para filtrar tickets pela data de fechamento. É possível passar uma variação de datas separada ','. Ex: 2014-12-15T11:00:00.000-02:00,2014-12-15T23:00:00.00-02:00. É possível também utilizar o caractere '*' para não limitar alguma posição. Ex: 2014-12-14T00:00.000-02:00,*. (required)
            _offset, int: Parâmetro utilizado para indicar a posição inicial de consulta.  (required)
            _limit, int: Parâmetro utilizado para limitar a quantidade de registros trazidos pela consulta.  (required)
            

        Returns: Tickets
        """

        allParams = ['status', 'code', 'customer_name', 'created_at', 'closed_at', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_tickets" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tickets'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('status' in params):
            queryParams['status'] = self.apiClient.toPathValue(params['status'])
        
        if ('code' in params):
            queryParams['code'] = self.apiClient.toPathValue(params['code'])
        
        if ('customer_name' in params):
            queryParams['customerName'] = self.apiClient.toPathValue(params['customer_name'])
        
        if ('created_at' in params):
            queryParams['createdAt'] = self.apiClient.toPathValue(params['created_at'])
        
        if ('closed_at' in params):
            queryParams['closedAt'] = self.apiClient.toPathValue(params['closed_at'])
        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Tickets')
        return responseObject
        
        
        
    
    def post_ticket(self, **kwargs):
        """Cria um novo protocolo
        <p>Esse serviço irá efetuar a criação de um novo Ticket. Serve para atender as necessidades do lojista entrar em contato com o consumidor final caso necessário.</p><p class='obs obs-danger'>Todo contato com o comprador, com exceção dos os emails transacionais que já são enviados pelo Marketplace, deve ser realizado através desta API.</p>

        Args:
            new_ticket, NewTicket: Objeto Novo Ticket.. (required)
            

        Returns: str
        """

        allParams = ['new_ticket']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_ticket" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tickets'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['new_ticket']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def put_ticket_assignee(self, **kwargs):
        """Operação utilizada para atualizar o responsável pelo atendimento do protocolo
        <p>Esse serviço permitirá atualizar o responsável pelo atendimento de um Ticket, onde as possibilidades são: Marketplace ou Lojista.</p>

        Args:
            code, str: Código do protocolo. (required)
            body, TicketAssignee: Mensagem a ser enviada como descrição da operação. (required)
            

        Returns: str
        """

        allParams = ['code', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_ticket_assignee" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tickets/{code}/assignee'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('code' in params):
            replacement = str(self.apiClient.toPathValue(params['code']))
            resourcePath = resourcePath.replace('{' + 'code' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def get_ticket_messages_by_code(self, **kwargs):
        """Operação utilizada para consultar um protocolo
        <p>Esse serviço apresenta todo o histórico de mensagens trocadas no Ticket para efetuar o atendimento. Para efetuar uma requisição é necessário passar o code do Ticket desejado no path do serviço.</p> <p class='obs'>Só serão exibidos os protocolos que sejam de propriedade do lojista/parceiro que está efetuando a consulta.</p>

        Args:
            code, str: Identificador do  protocolo. (required)
            _offset, int: Parâmetro utilizado para indicar a posição do registro inicial que será trazido. A primeira posição é sempre zero (0). (required)
            _limit, int: Parâmetro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: GetTicketMessagesResponse
        """

        allParams = ['code', '_offset', '_limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_ticket_messages_by_code" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tickets/{code}/messages'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('_offset' in params):
            queryParams['_offset'] = self.apiClient.toPathValue(params['_offset'])
        
        if ('_limit' in params):
            queryParams['_limit'] = self.apiClient.toPathValue(params['_limit'])
        

        

        
        if ('code' in params):
            replacement = str(self.apiClient.toPathValue(params['code']))
            resourcePath = resourcePath.replace('{' + 'code' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetTicketMessagesResponse')
        return responseObject
        
        
        
    
    def post_ticket_message(self, **kwargs):
        """Operação utilizada para criar uma mensagem no protocolo
        <p>Esse serviço irá criar uma mensagem atrelada ao Ticket em questão. Essa mensagem pode ou não ficar visível para o consumidor final. As mensagens enviadas ficam disponíveis no serviço de Consulta de Mensagens de Ticket.</p>

        Args:
            code, str: Identificador do  protocolo. (required)
            ticket, NewTicketMessage: Objeto Ticket. (required)
            

        Returns: str
        """

        allParams = ['code', 'ticket']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method post_ticket_message" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tickets/{code}/messages'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('code' in params):
            replacement = str(self.apiClient.toPathValue(params['code']))
            resourcePath = resourcePath.replace('{' + 'code' + '}',
                                                replacement)
        

        postData = params['ticket']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    
    def put_ticket_status(self, **kwargs):
        """Operação utilizada para atualizar o status dos tickets
        <p>Esse serviço permitirá que o lojista/plataforma altere o status de um Ticket. Os status permitidos serão: Fechado <strong> (closed) </strong> e Em Acompanhamento <strong> (attendance).</strong></p>

        Args:
            code, str: Código do protocólo. (required)
            body, TicketStatus: Parâmetros para ativação/desativação massiva de produtos (required)
            

        Returns: str
        """

        allParams = ['code', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method put_ticket_status" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tickets/{code}/status'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('code' in params):
            replacement = str(self.apiClient.toPathValue(params['code']))
            resourcePath = resourcePath.replace('{' + 'code' + '}',
                                                replacement)
        

        postData = params['body']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'str')
        return responseObject
        
        
        
    


