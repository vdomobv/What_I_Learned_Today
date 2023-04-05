create table contacts(
    name text not null,
    age integer not null,
    email text not null unique
);

alter table contacts rename to new_contacts;

alter table new_contacts rename COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN address text NOT NULL DEFAULT 'no address';

ALTER TABLE new_contacts DROP COLUMN address;

DROP TABLE new_contacts;

SELECT first_name, age FROM users;
SELECT * FROM users;
SELECT rowid, first_name FROM users;
SELECT first_name, age FROM users ORDER BY age;
SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;
