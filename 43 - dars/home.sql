CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount INT,

    CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO customers (name) VALUES
    ('Mahina'),
    ('Shahina'),
    ('Munisa'),
    ('Aziza'),
    ('Muslima'),
    ('Erkin'),
    ('Zubayr'),
    ('Muxsina')
    ('Soliha');


INSERT INTO orders (customer_id, order_date, total_amount) VALUES
  (1, '2025-07-30', 5),
  (2, '2025-07-29', 7),
  (3, '2025-07-29', 1),
  (4,'2025-06-29' , 6),
  (5, '2025-06-20', 3),
  (6, '2024-09-28', 2),
  (7, '2020-12-31', 9),
  (8, '2021-02-19', 10);

SELECT
  C.*,
  O.*
FROM customers AS C
  LEFT JOIN orders AS O
    ON C.ID = O.customer_id
WHERE EXTRACT(YEAR FROM O.order_date) = 2024;

CREATE TABLE IF NOT EXISTS employees2 (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    department_id INT,
    CONSTRAINT fk_department_id FOREIGN KEY (department_id) REFERENCES departments2(id)
);

CREATE TABLE IF NOT EXISTS departments2 (
    id SERIAL PRIMARY KEY,
    department_name VARCHAR(100)
);

INSERT INTO employees2 (name, department_id) VALUES
    ('Mahina', 1),
    ('Muslima', 2),
    ('Muhsina', 3),
    ('Zubayr', NULL),
    ('Muslim', NULL);

INSERT INTO departments2 (department_name) VALUES
    ('Marketing'),
    ('HR'),
    ('sales');

SELECT
 E.*,
 D.*
FROM employees2 as E
   LEFT JOIN departments2 as D
       ON D.id = E.department_id;

DELETE FROM employees2
USING departments2
where employees2.department_id = departments2.id
and departments2.department_name = 'Marketing';

CREATE TABLE IF NOT EXISTS teachers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS subjects(
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100),
    teacher_id INT,
    CONSTRAINT fk_teacher_id FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

INSERT INTO teachers (name) VALUES
    ('Mahina'),
    ('Muslima'),
    ('Muhsina'),
    ('Zubayr'),
    ('Muslim'),
    ('Soliha');

INSERT INTO subjects (subject_name, teacher_id) VALUES
    ('math', 1),
    ('english', 2),
    ('art', 3),
    ('pe', 4),
    ('russian', 5);

INSERT INTO subjects (subject_name, teacher_id) VALUES
    ('english', 5),
    ('art', 4),
    ('pe', 3),
    ('russian', 1);

select t.name, count(s.id) as subject_count from teachers as t left join subjects as s on s.teacher_id = t.id
group by t.id, t.name;

create table if not exists authors (
     id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

create table if not exists books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author_id INT,
    published_year SMALLINT,
    CONSTRAINT fk_author_id FOREIGN KEY (author_id) REFERENCES authors(id)
);
INSERT INTO authors (name) VALUES
  ('Jane Austen'),
  ('George Orwell'),
  ('Fyodor Dostoevsky'),
  ('Haruki Murakami'),
  ('Chimamanda Ngozi Adichie'),
  ('Gabriel García Márquez'),
  ('Leo Tolstoy'),
  ('Virginia Woolf'),
  ('J.K. Rowling'),
  ('Mark Twain'),
  ('Xudoyberdi Toxtaboyev');

INSERT INTO books (title, author_id, published_year) VALUES
  ('Pride and Prejudice', 1, 1813),
  ('1984', 2, 1949),
  ('Crime and Punishment', 3, 1866),
  ('Norwegian Wood', 4, 1987),
  ('Half of a Yellow Sun', 5, 2006),
  ('One Hundred Years of Solitude', 6, 1967),
  ('War and Peace', 7, 1869),
  ('Mrs Dalloway', 8, 1925),
  ('Harry Potter and the Philosopher Stone', 9, 1997),
  ('Adventures of Huckleberry Finn', 10, 1884);

select a.name, count(b.id) as book_count from authors as a left join books as b
on b.author_id = a.id
group by a.id, a.name;



