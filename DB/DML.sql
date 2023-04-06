CREATE TABLE users (
  first_name TEXT NOT null,
  last_name TEXT NOT null,
  age INTEGER NOT null,
  country TEXT NOT null,
  phone TEXT NOT null,
  balance INTEGER NOT null
);

SELECT * FROM users;

SELECT DISTINCT country FROM users;
DROP TABLE users;

-- 04.06
CREATE TABLE users(
  id integer PRIMARY KEY AUTOINCREMENT,
  name text NOT NULL,
  roleid integer NOT NULL
);

CREATE TABLE articles (
  id integer PRIMARY KEY AUTOINCREMENT,
  title text NOT NULL,
  content text NOT NULL,
  userid integer,
  CONSTRAINT userid_fk FOREIGN KEY(userid) REFERENCES users(id)
);

INSERT INTO users(name, roleid)
VALUES ('aiden', 1),
('aiden2', 2),
('aiden3', 3),
('aiden4', 4),
('aiden5', 5),
('aiden6', 6);

INSERT INTO articles(title, content, userid)
VALUES
('title1', 'content1', 1),
('title2', 'content2', 2),
('title3', 'content3', 3),
('title4', 'content4', 4),
('title5', 'content5', 5),
('title6', 'content6', 6);

INSERT INTO articles(title, content, userid)
VALUES ('t', 'c', 7);

SELECT articles.*, users.* FROM articles, users;

SELECT articles.*, users.* FROM articles JOIN users ON articles.userid = users.id;
SELECT articles.*, users.* FROM articles LEFT JOIN users ON articles.userid = users.id;
SELECT articles.*, users.* FROM articles RIGHT JOIN users ON articles.userid = users.id;

-- ACID
-- 원자성, 일관성, 독립성, 지속성
-- 1. 원자성 : 트랜잭션이 DB에 모두 반영되거나 혹은 모두 반영되지 않거나 둘 중 하나여야 한다.
-- 2. 일관성 : 트랜잭션의 처리 결과는 일관적이어야 한다.
-- 3. 독립성 : 둘 이상의 트랜잭션이 동시에 실행되고 있을 때, 어떤 한 트랜잭션이 다른 트랜잭션의 연산에 끼어들 수 없다.
-- 4. 지속성 : 트랜잭션이 성공적으로 완료되었다면, 결과는 영구적으로 반영되어야 한다.

-- sqlite는 기본적으로 autocommit되는 db
-- Begin 키워드를 사용하면 autocommit이 되지 않는다.
-- rollback 키워드는 트랜잭션 중간에 진행했던 작업 내역들을 모두 버리고 트랜잭션의 시작 상태로 돌아간다.
-- commit 키워드는 트랜잭션 완료, 트랜잭션 중간에 진행했던 작업 내역들을 모두 DB에 반영
