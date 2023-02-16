-- 문제 1

SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;
    
-- 문제 2

SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
LEFT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
    
-- 문제 3

SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
RIGHT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;

-- 문제 4
SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
INNER JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
    
-- 문제 5
-- 문제 2 customers , offices의 합에서 offices를 제외한 값 출력
-- 문제 3 customers , offices의 합에서 customers를 제외한 값 출력
-- 문제 3 customers , offices의 교집합 출력

-- 문제 6
SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
LEFT JOIN offices AS t2
	ON t1.city = t2.city
UNION
SELECT customerNumber, officeCode, t1.city, t2.city
FROM customers AS t1
RIGHT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
    
-- 문제 7

SELECT t1.orderNumber, orderDate
FROM orderdetails AS t1
INNER JOIN orders AS t2
	ON t1.orderNumber = t2.orderNumber
ORDER BY
	orderNumber;
    
-- 문제 8

SELECT orderNumber, t1.productCode, productName
FROM orderdetails AS t1
INNER JOIN products AS t2
	ON t1.productCode = t2.productCode
ORDER BY
	orderNumber;
    
-- 문제 9

SELECT t1.orderNumber, t1.productCode , orderDate, productName
FROM orderdetails AS t1
INNER JOIN orders AS t2
	ON t1.orderNumber = t2.orderNumber
INNER JOIN products AS t3
	ON t1.productCode = t3.productCode
ORDER BY
	orderNumber;