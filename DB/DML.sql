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