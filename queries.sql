#Q1
SELECT
  COUNT(SalesOrderID)
FROM
  `rox-bike.BIKE.SalesOrderDetail`
WHERE
  OrderQty > 2;

#Q2
SELECT P.Name, SUM(O.OrderQty) As Vendas 
FROM `rox-bike.BIKE.Product` AS P 
INNER JOIN `rox-bike.BIKE.SpecialOfferProduct` AS S 
    ON P.ProductID=S.ProductID
INNER JOIN `rox-bike.BIKE.SalesOrderDetail` AS O 
    ON S.ProductID=O.ProductID
GROUP BY P.DaysToManufacture, P.Name, O.OrderQty
ORDER BY  O.OrderQty DESC
LIMIT 3;

#Q3
SELECT  P.FirstName, P.LastName, COUNT(H.CustomerID) AS Pedidos
FROM `rox-bike.BIKE.Person` AS P 
INNER JOIN `rox-bike.BIKE.Customer` AS C 
    ON P.BusinessEntityID=C.PersonID
INNER JOIN `rox-bike.BIKE.SalesOrderHeader` AS H
    ON C.CustomerID=H.CustomerID
GROUP BY H.CustomerID, P.FirstName, P.LastName
ORDER BY Pedidos DESC;

#Q4
SELECT  P.ProductID, H.OrderDate, SUM(D.OrderQty) AS SOMAPRODUTOS
FROM `rox-bike.BIKE.SalesOrderDetail` AS D 
INNER JOIN `rox-bike.BIKE.SalesOrderHeader` AS H 
    ON D.SalesOrderID=H.SalesOrderID
INNER JOIN `rox-bike.BIKE.Product` AS P
    ON D.ProductID=P.ProductID
GROUP BY P.ProductID, H.OrderDate, D.OrderQty;

#Q5
SELECT  H.SalesOrderID, H.OrderDate, H.TotalDue
FROM `rox-bike.BIKE.SalesOrderHeader` AS H 
WHERE H.TotalDue > 1000 AND H.OrderDate BETWEEN "2011-09-01" AND "2011-09-30"
ORDER BY H.TotalDue DESC;
