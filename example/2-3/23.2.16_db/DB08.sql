SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM products;
SELECT * FROM orderdetails;
-- 문제 1
SELECT
	productCode, productName, MSRP
FROM 
	products
WHERE MSRP >(
    SELECT AVG(MSRP)
    FROM products
)
ORDER BY
	MSRP;
    
-- 문제 2

SELECT
	customerNumber, customerName
FROM
	customers
WHERE customerNumber IN(
	SELECT customerNumber
    FROM orders
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY
	customerNumber;

-- 문제 3

SELECT
	productCode, productName, productLine, MSRP
FROM
	products
WHERE MSRP =(
	SELECT max(MSRP)
    FROM products
    WHERE productLine = 'Classic Cars'
);

-- 문제 4

SELECT
	customerNumber, customerName, country
FROM
	customers
WHERE country = (
	SELECT MAX(country)
	FROM customers
);
  

-- 문제 5
SELECT
	orders.customerNumber, customerName, count(*) AS order_count
FROM
	orders
INNER JOIN
	customers
    on orders.customerNumber = customers.customerNumber
GROUP BY
    customerNumber
ORDER BY
	order_count DESC
LIMIT
	1;
    
-- 문제 6

SELECT DISTINCT
	products.productCode, productName
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
WHERE orders.orderNumber IN(
	SELECT orderNumber
    FROM orders
    WHERE YEAR(orderDate) = '2004'
)
ORDER BY
	productCode DESC;