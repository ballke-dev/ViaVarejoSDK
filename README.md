# SDK Python para API V2 de Lojistas

Provê os componentes Python para uso da API V2 de lojistas, disponibilizada pela CNova.

![Vantagens na utilização de SDKs](https://desenvolvedores.cnova.com/api-portal/sites/default/files/images/sdk_dev.png)

## Criando um API Client

Antes de utilizar as APIs, é necessário a criação de um client com as configurações de _base path_ e também as credenciais para acesso.

Abaixo segue o código de exemplo:

```python3
import json

from cnova_api_lojista_v2 import *
from cnova_api_lojista_v2.api import *
from cnova_api_lojista_v2.model import *
from cnova_api_lojista_v2.client import ApiClient

from urllib.error import HTTPError
from datetime import datetime

apiClient = client.ApiClient (
                {
                    # Alterar a chave informada com o valor de client_id disponível para sua APP
                    'client_id' : 'll0rQx9SSshr',
                    # Alterar a chave informada com o valor de access_token disponível para sua APP
                    'access_token' : 'nllKgtXTMv0G'
                },
                'https://sandbox.cnova.com/api/v2')
```

## Operações auxiliares

Tratamento de estruturas de erros recebidas nas chamadas à API:

```python3
def deserialize_errors(errorsJson, apiClient):

    obj = None
    
    try:
        data = json.loads(errorsJson)
        obj = apiClient.deserialize(data, 'Errors')
    except ValueError:  # PUT requests don't return anything
        obj = None

    return obj
```

Formatação de datas para consultas em períodos específicos:

```python3
def format_date_range(initialDate, finalDate, apiClient):
    
    def x(a):
        print(a)

    dt_ini = '*'
    dt_end = '*'

    if (initialDate != None and type(initialDate) == datetime):
        dt_ini = apiClient.sanitizeForSerialization(initialDate)

    if (finalDate != None and type(finalDate) == datetime):
        dt_end = apiClient.sanitizeForSerialization(finalDate)

    return dt_ini + ',' + dt_end
```

## APIs Disponíveis

A seguir, são apresentadas as APIs e exemplos com as as principais operações do Marketplace.

### Loads API

API utilizada para operações de carga.

Carga de produtos:

```python3
product = Product.Product()
product.sku_seller_id = 'CEL_MOTO_X'
product.product_seller_id = 'CEL'
product.title = 'Produto de testes Motorola Moto X'
product.description = '<h2>O novo produto de testes</h2>, Moto X'
product.brand = 'Motorola'
product.gtin = ['123456ft']
product.categories  = ['Teste>API']
product.images  = ['http://img.g.org/img1.jpeg']
       
prices = ProductLoadPrices.ProductLoadPrices()
prices.default = 1999
prices.offer = 1799
     
product.price = prices
   
stock = ProductLoadStock.ProductLoadStock()
stock.quantity  = 100
stock.cross_docking_time = 0
    
product.stock  = stock
   
dimensions = Dimensions.Dimensions()
dimensions.weight = 10
dimensions.length = 10
dimensions.width = 10
dimensions.height = 10
     
product.dimensions = dimensions
     
product_attribute = ProductAttribute.ProductAttribute()
product_attribute.name  = 'cor'
product_attribute.value = 'Verde'
   
product.attributes = [product_attribute]
   
product_list = [product]
   
try:
       
    loads_api = LoadsApi.LoadsApi(apiClient)
    loads_api.post_products(products = product_list)
   
except HTTPError as e:
       
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
       
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(e.msg)
```

Consulta de cargas enviadas:

```python3
try:
     
    loads_api = LoadsApi.LoadsApi(apiClient)
    get_products_response = loads_api.get_products(_offset = 0, _limit = 100);
    print(vars(get_products_response))
   
except HTTPError as e:
         
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
         
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(e.msg)
```

Consulta um produto específico da carga enviada:

```python3
try:
    
    loads_api = LoadsApi.LoadsApi(apiClient)
    get_product_with_errors_response = loads_api.get_product(sku_seller_id = 'CEL_LGFlex')
    
    print(vars(get_product_with_errors_response))
    
except HTTPError as e:
         
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
         
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(e.msg)
```

Modificação do tracking de uma ou mais ordens, utilizando a API Loads:

```python3
orders_trackings = OrdersTrackings.OrdersTrackings()
     
order_tracking = OrderTracking.OrderTracking()
     
order_id = OrderId.OrderId()
order_id.id = 123
     
order_tracking.order = order_id
order_tracking.control_point = 'ABC'
order_tracking.cte = '123'
     
oif = OrderItemReference.OrderItemReference()
oif.sku_seller_id = '123456'
oif.quantity = 1
      
order_tracking.items = [oif]
  
order_tracking.occurred_at = datetime.now()
order_tracking.seller_delivery_id = '99995439701'
order_tracking.number = '01092014'
order_tracking.url = 'servico envio2'
      
carrier = Carrier.Carrier()
carrier.cnpj = '72874279234'
carrier.name = 'Sedex'
      
order_tracking.carrier = carrier
      
invoice = Invoice.Invoice()
invoice.cnpj = '72874279234'
invoice.number = '123'
invoice.serie = '456'
invoice.issued_at = datetime.now()
invoice.access_key = '01091111111111111111111111111111111111101092'
invoice.link_xml = 'link xlm teste5'
invoice.link_danfe = 'link nfe teste5'
      
order_tracking.invoice = invoice
   
orders_trackings.trackings = [order_tracking]
 
print(json.dumps(apiClient.sanitizeForSerialization(orders_trackings)))
   
try:
       
    loads_api = LoadsApi.LoadsApi(apiClient)
    loads_api.post_orders_tracking_sent(orders_trackings = orders_trackings)
   
except HTTPError as e:
           
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
           
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(e.msg)
```

### Seller Items API

API utilizada para gerenciamento dos recursos enviados pelo lojista.

Consulta de seller items:

```python3
try:
     
    seller_items_api = SellerItemsApi.SellerItemsApi(apiClient)
    get_seller_items_response = seller_items_api.get_seller_items(site = 'EX', _offset = 0, _limit = 100);
     
    print(vars(get_seller_items_response))
 
except HTTPError as e:
 
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
           
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(e.msg)
```

Alteração de preço:

```python3
try:
 
    prices = Prices.Prices()
    prices.default = 100
    prices.offer = 100
 
    seller_items_api = SellerItemsApi.SellerItemsApi(apiClient)
    seller_items_api.put_seller_item_prices(sku_seller_id = '31.0019', body = prices)
 
except HTTPError as e:
    print(e.msg)
```

Alteração de estoque:

```python3
try:

    stock = Stock.Stock()
    stock.quantity = 200
    stock.cross_docking_time = 0

    seller_items_api = SellerItemsApi.SellerItemsApi(apiClient)
    seller_items_api.put_seller_item_stock(sku_seller_id = '31.0019', body = stock)

except HTTPError as e:
    print(e.msg)
```

### Orders API

API utilizada para gerenciamento de pedidos.

Consulta todas as ordens:

```python3
try:
      
    orders_api = OrdersApi.OrdersApi(apiClient)
    get_orders_response = orders_api.get_orders(_offset = 0, _limit = 100);
    print(vars(get_orders_response))
      
except HTTPError as e:
    print(e.msg)
```

Consulta todas as ordens com status "novo":

```python3
try:
      
    purchased_at = format_date_range(None, datetime.now(), apiClient)
          
    orders_api = OrdersApi.OrdersApi(apiClient)
    get_orders_status_new_response =  orders_api.get_orders_by_status_new(_offset = 0, _limit = 100, purchased_at = purchased_at)
    print(vars(get_orders_status_new_response))
      
except HTTPError as e:
    print(e.msg)
```

Criação de um novo tracking, notificando o envio da ordem:

```python3
new_tracking = NewTracking.NewTracking()
   
new_tracking.items = ['23258312-1' ,'23258312-2']
   
new_tracking.occurred_at = datetime.now()
   
new_tracking.seller_delivery_id = '99995439701'
new_tracking.number = '01092014'
new_tracking.url = 'servico envio2'
   
carrier = Carrier.Carrier()
carrier.cnpj = '72874279234'
carrier.name = 'Sedex'
   
new_tracking.carrier = carrier
   
invoice = Invoice.Invoice()
invoice.cnpj = '72874279234'
invoice.number = '123'
invoice.serie = '456'
invoice.issued_at = datetime.now()
invoice.access_key = '01091111111111111111111111111111111111101092'
invoice.link_xml = 'link xlm teste5'
invoice.link_danfe = 'link nfe teste5'
   
new_tracking.invoice = invoice
   
try:
       
    orders_api = OrdersApi.OrdersApi(apiClient)
    orders_api.post_order_tracking_sent(order_id = '1024101', body = new_tracking);
       
except HTTPError as e:
             
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
             
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(e.msg)
```

Consulta de ordens com status "enviado":

```python3
try:
       
    orders_api = OrdersApi.OrdersApi(apiClient)
   
    get_orders_response = orders_api.get_orders_by_status_sent(_offset = 0, _limit = 100, customer_name = 'Joao')
    print(vars(get_orders_response))
   
except HTTPError as e:
    print(e.msg)
```

### Tickets API

API utilizada para gerenciamento de tickets.

Criação de um novo ticket:

```python3
new_ticket = NewTicket.NewTicket()
new_ticket.to = 'atendimento+OS_706000500000@mktp.extra.com.br'
new_ticket.body = 'Corpo da mensagem do ticket'
 
try:
     
    ticket_api = TicketsApi.TicketsApi(apiClient)
    ticket_api.post_ticket(new_ticket = new_ticket)
     
except HTTPError as e:
              
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
              
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(str(e.code) + '-' + e.msg)
```

Consulta ticket com status "Aberto":

```python3
try:
   
    tickets_api = TicketsApi.TicketsApi(apiClient)
     
    tickets = tickets_api.get_tickets(status = 'opened', code = '439211092852', _offset = 0, _limit = 5)
    print(vars(tickets))
   
except HTTPError as e:
    print(str(e.code) + '-' + e.msg) 
```

Alteração do status do ticket:

```python3
try:
 
    ticket_status = TicketStatus.TicketStatus()
    ticket_status.ticket_status = 'Em Acompanhamento'
     
    tickets_api = TicketsApi.TicketsApi(apiClient)
    tickets_api.put_ticket_status(code = '123123', body = ticket_status)
  
except HTTPError as e:
 
    errorList = deserialize_errors(e.fp.read().decode('utf-8'), apiClient)
 
    if errorList != None:
        for error in errorList.errors:
            print(error.code + ' - ' + error.message)
    else:
        print(str(e.code) + '-' + e.msg)
```

### Categories API

API utilziada na obtenção da árvore de categorias disponível.

Consulta as categorias disponíveis:

```python3 
try:
    
    categories_api = CategoriesApi.CategoriesApi(apiClient)
    get_categories_response = categories_api.get_categories(_offset = 0, _limit = 100)
     
    for categorie in get_categories_response.categories:
        print(str(categorie.id) + ' - ' + categorie.name)
        
except HTTPError as e:
    print(str(e.code) + '-' + e.msg) 
```

### Sites API

API utilizada na obtenção da lista de sites.

Consulta os sites disponíveis:

```python3 
try:
    
    sitesApi = SitesApi.SitesApi(apiClient)
    resp = sitesApi.get_sites()
      
    print( vars(resp) )

except HTTPError as e:
    print(str(e.code) + '-' + e.msg) 
```

### Warehouses API

API utilizada na obtenção da lista de warehouses (armazéns).

Consulta as warehouses disponíveis:

```python3 
try:
     
    warehouse_api = WarehousesApi.WarehousesApi(apiClient)
    get_warehouses_response = warehouse_api.get_warehouses()
       
    print(vars(get_warehouses_response))
         
except HTTPError as e:
    print(str(e.code) + '-' + e.msg) 
```