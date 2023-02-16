SHOW COLUMNS FROM users;
SELECT
	*
FROM
	users;
DROP TABLE users;

-- 문제 1

CREATE TABLE users (
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT null,
    last_name VARCHAR(20) NOT null,
    birthday DATE NOT null,
    city VARCHAR(100) null,
    country VARCHAR(100) null,
    email VARCHAR(100) null,
    created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);

-- 문제 2

INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01', Null , Null, 'beemo@hphk.kr'),
	('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', Null),
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', NULL),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', Null);
    
-- 문제 3
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
	('name1', 'name1', '1001-01-01', 'Seoul', 'Korea', 'a@a.a'),
    ('name2', 'name2', '1002-01-01', 'Seoul', 'Korea', 'b@a.a'),
    ('name3', 'name3', '1003-01-01', 'Seoul', 'Korea', 'c@a.a'),
    ('name4', 'name4', '1004-01-01', 'Seoul', 'Korea', 'd@a.a'),
    ('name5', 'name5', '1005-01-01', 'Seoul', 'Korea', 'e@a.a');
    
-- 문제 4
UPDATE
	users
SET
	first_name = 'Yuyoung',
    last_name = 'Seo',
    birthday = '1991-02-26'
WHERE
	userId = 2;
    
-- 문제 5
UPDATE
	users
SET
	country = 'Korea'
WHERE
	country IS NULL;

-- 문제 6
DELETE FROM
	users
WHERE
	first_name = 'Beemo';
    
-- 문제 7
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo'
    AND last_name='Lee';
    
-- 문제 8
DELETE FROM
	users
ORDER BY
	created_at DESC
lIMIT
	1;