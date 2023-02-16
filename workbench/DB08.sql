SELECT * FROM payments;

SELECT MAX(amount)
FROM payments;

SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);

SELECT lastName, firstName
FROM employees
WHERE officeCode IN
	(
	SELECT officeCode
    FROM offices
    WHERE country = 'USA'
);

SELECT * FROM customers;
SELECT * FROM orders;

SELECT customerName
FROM customers
WHERE customerNumber NOT IN	(
	SELECT DISTINCT customerNumber
    FROM orders
);


SELECT customerNumber, amount, contactFirstName
FROM (
	SELECT payments.customerNumber, amount, contactFirstName
	FROM payments
    INNER JOIN customers
		ON payments.customerNumber = customers.customerNumber
) AS mysub
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);

SELECT customerNumber, customerName
FROM customers
WHERE EXISTS (
	SELECT *
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber
);


SELECT * FROM employees;
SELECT * FROM offices;

SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS (
	SELECT *
    FROM offices
    WHERE city = 'Paris' AND employees.officeCode = offices.officeCode
);

SELECT contactFirstName, creditLimit,
	CASE
		WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platunum'
        ELSE 'Bronze'
    END AS grade
FROM customers;

SELECT orderNumber, status,
	CASE
		WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
	END AS details
FROM orders;