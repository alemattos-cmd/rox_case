## created by Alessandro de Mattos Silva
## 02/06/2021
## alemattos-cmd

import pyodbc
server = '<server>.database.windows.net'
database = '<rox_bike>'
username = '<sa>'
password = '<admin>'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
##    con = pymssql.connect(host = 'servidor',
##                          user = 'usuario',
##                         password = 'senha',
##                          database = 'base de dados')
## cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)', (valor1, valor2, valor3))
## con.commit()
## rs = cursor.fetchone() # busca uma linha ou;
## rs = cursor.fetchall() # busca todas as linhas ou;
## rs = cursor.dictfetchall() # busca todas as linhas,



## Análise de Dados

## 1.	Escreva uma query que retorna a quantidade de linhas na tabela Sales.SalesOrderDetail pelo campo SalesOrderID, 
##      desde que tenham pelo menos três linhas de detalhes.

## 2.	Escreva uma query que ligue as tabelas Sales.SalesOrderDetail, Sales.SpecialOfferProduct e Production.Product
##      e retorne os 3 produtos (Name) mais vendidos (pela soma de OrderQty), agrupados pelo número de dias para manufatura (DaysToManufacture).

## 3.	Escreva uma query ligando as tabelas Person.Person, Sales.Customer e Sales.SalesOrderHeader de forma a obter uma lista de nomes de clientes e 
##      uma contagem de pedidos efetuados.

## 4.	Escreva uma query usando as tabelas Sales.SalesOrderHeader, Sales.SalesOrderDetail e Production.Product, de forma a obter 
##      a soma total de produtos (OrderQty) por ProductID e OrderDate.

## 5.	Escreva uma query mostrando os campos SalesOrderID, OrderDate e TotalDue da tabela Sales.SalesOrderHeader. 
##      Obtenha apenas as linhas onde a ordem tenha sido feita durante o mês de setembro/2011 e o total devido esteja acima de 1.000. 
##      Ordene pelo total devido decrescente.

