SHOW COLUMNS FROM posts;

-- 문제 1
CREATE TABLE posts (
	postId INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT null,
    PRIMARY KEY (postId)
);

-- 문제 2
ALTER TABLE	posts
ADD	writer VARCHAR(100) NULL DEFAULT 'Anonymous',
ADD created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP;
-- CURRENT_TIMESTAMP = 생성 시간 자동 기록

-- 문제 3
ALTER TABLE
	posts
MODIFY
	content TEXT NULL;

-- 문제 4
ALTER TABLE
	posts
DROP COLUMN
	writer;

-- 문제 5
DROP TABLE posts;

-- 문제 6
CREATE TABLE IF NOT EXISTS posts (
	postId INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT null,
    writer VARCHAR(20) NOT NULL,
    created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (postID)
);

-- 문제 7

DROP TABLE 
IF EXISTS posts;