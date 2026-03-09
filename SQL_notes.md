# 🗄️ SQL Notes for Beginners

![Level](https://img.shields.io/badge/Level-Beginner--friendly-blue)
![Focus](https://img.shields.io/badge/Focus-Interviews-success)
![Format](https://img.shields.io/badge/Format-GitHub%20README-black)
![Examples](https://img.shields.io/badge/Includes-Real%20Life%20Examples-orange)
![Status](https://img.shields.io/badge/Use-Revision%20%2B%20Interview%20Prep-brightgreen)

> Clean, organized, beginner-friendly SQL notes with explanations, examples, and interview-focused concepts.  
> Made for **quick revision, practice, projects, viva, and interviews**.

---

## 📚 Table of Contents

- [1. What is SQL?](#1-what-is-sql)
- [2. Why Learn SQL?](#2-why-learn-sql)
- [3. Real-Life Uses of SQL](#3-real-life-uses-of-sql)
- [4. Databases, DBMS, and RDBMS](#4-databases-dbms-and-rdbms)
- [5. SQL Categories](#5-sql-categories)
- [6. Setting Up SQL](#6-setting-up-sql)
- [7. Database Basics](#7-database-basics)
- [8. Tables, Rows, and Columns](#8-tables-rows-and-columns)
- [9. Data Types in SQL](#9-data-types-in-sql)
- [10. Creating a Database and Table](#10-creating-a-database-and-table)
- [11. Inserting Data](#11-inserting-data)
- [12. Selecting Data](#12-selecting-data)
- [13. Filtering with WHERE](#13-filtering-with-where)
- [14. Comparison, Logical, and Special Operators](#14-comparison-logical-and-special-operators)
- [15. Sorting with ORDER BY](#15-sorting-with-order-by)
- [16. Limiting Results](#16-limiting-results)
- [17. Updating Data](#17-updating-data)
- [18. Deleting Data](#18-deleting-data)
- [19. NULL Values](#19-null-values)
- [20. Constraints](#20-constraints)
- [21. Primary Key and Foreign Key](#21-primary-key-and-foreign-key)
- [22. ALTER, DROP, and TRUNCATE](#22-alter-drop-and-truncate)
- [23. Aggregate Functions](#23-aggregate-functions)
- [24. GROUP BY](#24-group-by)
- [25. HAVING](#25-having)
- [26. DISTINCT](#26-distinct)
- [27. LIKE and Wildcards](#27-like-and-wildcards)
- [28. IN, BETWEEN, and EXISTS](#28-in-between-and-exists)
- [29. Joins](#29-joins)
- [30. Self Join](#30-self-join)
- [31. Set Operations](#31-set-operations)
- [32. Subqueries](#32-subqueries)
- [33. Correlated Subqueries](#33-correlated-subqueries)
- [34. Views](#34-views)
- [35. Indexes](#35-indexes)
- [36. SQL Functions](#36-sql-functions)
- [37. String Functions](#37-string-functions)
- [38. Date and Time Functions](#38-date-and-time-functions)
- [39. Numeric Functions](#39-numeric-functions)
- [40. CASE Statement](#40-case-statement)
- [41. Stored Procedures](#41-stored-procedures)
- [42. Triggers](#42-triggers)
- [43. Transactions](#43-transactions)
- [44. ACID Properties](#44-acid-properties)
- [45. Normalization](#45-normalization)
- [46. Denormalization](#46-denormalization)
- [47. Common SQL Commands for Projects](#47-common-sql-commands-for-projects)
- [48. SQL in Real-Life Projects](#48-sql-in-real-life-projects)
- [49. Common Interview Questions](#49-common-interview-questions)
- [50. Quick Revision Sheet](#50-quick-revision-sheet)

---

## 1. What is SQL?

SQL stands for **Structured Query Language**.

It is a language used to:
- create databases
- create tables
- store data
- retrieve data
- update data
- delete data
- manage relationships between tables

### Simple definition

SQL is the language used to talk to relational databases.

### Real-life example

Suppose you have a hospital system with:
- patient details
- doctor details
- appointments
- bills

SQL helps you:
- add a new patient
- find all appointments for today
- update bill amount
- show total revenue

---

## 2. Why Learn SQL?

SQL is important because data is everywhere.

Almost every software system stores information in a database:
- student management systems
- hospital management systems
- banking systems
- e-commerce websites
- social media platforms
- HR systems

### Why SQL is useful
- easy to learn compared to many programming topics
- used in software development, data analysis, backend, and testing
- required in interviews
- necessary for projects
- useful in real-world applications

### Real-life example

In an online shopping app, SQL is used to:
- store products
- save customer orders
- check stock
- calculate sales reports

---

## 3. Real-Life Uses of SQL

### Common applications

- **Hospital Management System** → patients, doctors, appointments, bills
- **College Database** → students, marks, attendance, departments
- **Banking System** → customers, accounts, transactions
- **E-Commerce** → products, orders, payments, reviews
- **Social Media** → users, posts, comments, likes
- **Job Portal** → candidates, resumes, job postings
- **Library Management** → books, issue records, fines

---

## 4. Databases, DBMS, and RDBMS

### Database
A database is an organized collection of data.

### DBMS
DBMS stands for **Database Management System**.

It is software used to manage databases.

Examples:
- MySQL
- PostgreSQL
- Oracle
- SQLite
- SQL Server

### RDBMS
RDBMS stands for **Relational Database Management System**.

It stores data in the form of **tables** and allows relationships between them.

### Real-life example

In a college:
- one table stores students
- one table stores courses
- one table stores marks

These tables can be linked using relationships.

---

## 5. SQL Categories

SQL commands are mainly divided into categories.

### 1. DDL – Data Definition Language
Used to define database structure.

Commands:
- `CREATE`
- `ALTER`
- `DROP`
- `TRUNCATE`

---

### 2. DML – Data Manipulation Language
Used to modify table data.

Commands:
- `INSERT`
- `UPDATE`
- `DELETE`

---

### 3. DQL – Data Query Language
Used to fetch data.

Command:
- `SELECT`

---

### 4. DCL – Data Control Language
Used to control access.

Commands:
- `GRANT`
- `REVOKE`

---

### 5. TCL – Transaction Control Language
Used to manage transactions.

Commands:
- `COMMIT`
- `ROLLBACK`
- `SAVEPOINT`

---

## 6. Setting Up SQL

Common database systems:
- MySQL
- PostgreSQL
- SQLite
- Microsoft SQL Server
- Oracle Database

### Popular tools
- MySQL Workbench
- pgAdmin
- DBeaver
- DB Browser for SQLite
- phpMyAdmin

### Beginner-friendly option
- MySQL or SQLite

---

## 7. Database Basics

A database contains one or more tables.

Example: `hospital_db`

Inside it:
- `patients`
- `doctors`
- `appointments`
- `bills`

Each table stores related data.

---

## 8. Tables, Rows, and Columns

A table looks like a spreadsheet.

### Example: `students`

| student_id | name  | age | department |
|------------|-------|-----|------------|
| 1          | Alina | 21  | CSE        |
| 2          | Ravi  | 22  | ECE        |

### Terms
- **Table** → full structure
- **Row / Record** → one entry
- **Column / Field** → one attribute

---

## 9. Data Types in SQL

Different SQL databases may have slightly different names, but common types are:

### Numeric Types
- `INT`
- `BIGINT`
- `DECIMAL`
- `FLOAT`
- `DOUBLE`

### Character Types
- `CHAR`
- `VARCHAR`
- `TEXT`

### Date and Time Types
- `DATE`
- `TIME`
- `DATETIME`
- `TIMESTAMP`

### Boolean Type
- `BOOLEAN`

### Example
```sql
age INT,
name VARCHAR(100),
salary DECIMAL(10,2),
joined_date DATE
```

### Real-life example
In an employee table:
- employee ID → `INT`
- name → `VARCHAR`
- salary → `DECIMAL`
- joining date → `DATE`

---

## 10. Creating a Database and Table

### Create database
```sql
CREATE DATABASE college_db;
```

### Use database
```sql
USE college_db;
```

### Create table
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);
```

### Explanation
- `student_id` uniquely identifies each student
- `VARCHAR(100)` stores text up to 100 characters
- `PRIMARY KEY` means no duplicate and no null

---

## 11. Inserting Data

### Insert one row
```sql
INSERT INTO students (student_id, name, age, department)
VALUES (1, 'Alina', 21, 'CSE');
```

### Insert multiple rows
```sql
INSERT INTO students (student_id, name, age, department)
VALUES
(2, 'Ravi', 22, 'ECE'),
(3, 'Meera', 20, 'ISE'),
(4, 'John', 23, 'CSE');
```

### Real-life example
When a new student joins college, their details are inserted into the `students` table.

---

## 12. Selecting Data

### Select all columns
```sql
SELECT * FROM students;
```

### Select specific columns
```sql
SELECT name, department FROM students;
```

### Why `SELECT` matters
This is the most used SQL command because most applications need to read data frequently.

---

## 13. Filtering with WHERE

`WHERE` is used to filter rows.

### Example
```sql
SELECT * FROM students
WHERE department = 'CSE';
```

### Another example
```sql
SELECT * FROM students
WHERE age > 21;
```

### Real-life example
Show all patients whose age is above 60:
```sql
SELECT * FROM patients
WHERE age > 60;
```

---

## 14. Comparison, Logical, and Special Operators

### Comparison operators
- `=`
- `!=` or `<>`
- `>`
- `<`
- `>=`
- `<=`

### Logical operators
- `AND`
- `OR`
- `NOT`

### Example
```sql
SELECT * FROM students
WHERE department = 'CSE' AND age > 20;
```

### Example with OR
```sql
SELECT * FROM students
WHERE department = 'CSE' OR department = 'ISE';
```

### Example with NOT
```sql
SELECT * FROM students
WHERE NOT department = 'ECE';
```

---

## 15. Sorting with ORDER BY

`ORDER BY` is used to sort results.

### Ascending order
```sql
SELECT * FROM students
ORDER BY age ASC;
```

### Descending order
```sql
SELECT * FROM students
ORDER BY age DESC;
```

### Sort by multiple columns
```sql
SELECT * FROM students
ORDER BY department ASC, age DESC;
```

### Real-life example
List highest salary employees first:
```sql
SELECT * FROM employees
ORDER BY salary DESC;
```

---

## 16. Limiting Results

Different databases use different syntax.

### MySQL / PostgreSQL
```sql
SELECT * FROM students
LIMIT 5;
```

### SQL Server
```sql
SELECT TOP 5 * FROM students;
```

### Real-life example
Show top 10 latest orders:
```sql
SELECT * FROM orders
ORDER BY order_date DESC
LIMIT 10;
```

---

## 17. Updating Data

`UPDATE` is used to modify existing rows.

### Example
```sql
UPDATE students
SET age = 22
WHERE student_id = 1;
```

### Update multiple columns
```sql
UPDATE students
SET age = 23, department = 'AI&ML'
WHERE student_id = 2;
```

### Warning
If you forget the `WHERE` clause, all rows may get updated.

### Bad example
```sql
UPDATE students
SET department = 'CSE';
```

This changes every row.

---

## 18. Deleting Data

`DELETE` is used to remove rows.

### Example
```sql
DELETE FROM students
WHERE student_id = 4;
```

### Warning
Without `WHERE`, all rows are deleted.

```sql
DELETE FROM students;
```

This deletes every record but keeps the table structure.

---

## 19. NULL Values

`NULL` means missing or unknown value.

It does **not** mean:
- zero
- empty string
- false

### Example
A student may not yet have a phone number.

### Check null values
```sql
SELECT * FROM students
WHERE phone_number IS NULL;
```

### Check not null
```sql
SELECT * FROM students
WHERE phone_number IS NOT NULL;
```

---

## 20. Constraints

Constraints are rules applied to columns.

### Common constraints
- `PRIMARY KEY`
- `FOREIGN KEY`
- `NOT NULL`
- `UNIQUE`
- `CHECK`
- `DEFAULT`

### Example
```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    city VARCHAR(50) DEFAULT 'Bangalore'
);
```

### Why constraints matter
They protect data quality.

---

## 21. Primary Key and Foreign Key

### Primary Key
Uniquely identifies each row in a table.

Example:
- `student_id`
- `patient_id`
- `order_id`

### Foreign Key
A column that refers to the primary key of another table.

### Example

```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

### Real-life example
A student belongs to one department.  
`dept_id` in `students` links to `departments`.

---

## 22. ALTER, DROP, and TRUNCATE

### ALTER
Used to change table structure.

#### Add column
```sql
ALTER TABLE students
ADD email VARCHAR(100);
```

#### Modify column
```sql
ALTER TABLE students
MODIFY age INT;
```

#### Drop column
```sql
ALTER TABLE students
DROP COLUMN email;
```

---

### DROP
Deletes the entire table structure and data.

```sql
DROP TABLE students;
```

---

### TRUNCATE
Deletes all rows but keeps the table structure.

```sql
TRUNCATE TABLE students;
```

### Difference
- `DELETE` → removes rows, can use `WHERE`
- `TRUNCATE` → removes all rows quickly, no `WHERE`
- `DROP` → removes table itself

---

## 23. Aggregate Functions

Aggregate functions perform calculations on multiple rows.

### Common aggregate functions
- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

### Examples
```sql
SELECT COUNT(*) FROM students;
```

```sql
SELECT AVG(age) FROM students;
```

```sql
SELECT MAX(age) FROM students;
```

```sql
SELECT SUM(salary) FROM employees;
```

### Real-life example
Find total sales:
```sql
SELECT SUM(total_amount) FROM orders;
```

---

## 24. GROUP BY

`GROUP BY` groups rows with the same values.

### Example
```sql
SELECT department, COUNT(*) AS total_students
FROM students
GROUP BY department;
```

### Another example
```sql
SELECT department, AVG(age) AS avg_age
FROM students
GROUP BY department;
```

### Real-life example
Show number of patients by gender:
```sql
SELECT gender, COUNT(*) AS total_patients
FROM patients
GROUP BY gender;
```

---

## 25. HAVING

`HAVING` filters grouped results.

### Example
```sql
SELECT department, COUNT(*) AS total_students
FROM students
GROUP BY department
HAVING COUNT(*) > 2;
```

### Difference between WHERE and HAVING
- `WHERE` filters rows before grouping
- `HAVING` filters groups after grouping

---

## 26. DISTINCT

`DISTINCT` removes duplicates from output.

### Example
```sql
SELECT DISTINCT department
FROM students;
```

### Real-life example
Find all unique cities of customers:
```sql
SELECT DISTINCT city
FROM customers;
```

---

## 27. LIKE and Wildcards

`LIKE` is used for pattern matching.

### Wildcards
- `%` → any number of characters
- `_` → one single character

### Example: names starting with A
```sql
SELECT * FROM students
WHERE name LIKE 'A%';
```

### Example: names ending with a
```sql
SELECT * FROM students
WHERE name LIKE '%a';
```

### Example: names containing 'in'
```sql
SELECT * FROM students
WHERE name LIKE '%in%';
```

### Example: exactly 5-letter names starting with A
```sql
SELECT * FROM students
WHERE name LIKE 'A____';
```

---

## 28. IN, BETWEEN, and EXISTS

### IN
Used to check multiple possible values.

```sql
SELECT * FROM students
WHERE department IN ('CSE', 'ISE', 'ECE');
```

### BETWEEN
Used for ranges.

```sql
SELECT * FROM students
WHERE age BETWEEN 20 AND 22;
```

### EXISTS
Checks if a subquery returns any row.

```sql
SELECT name
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM departments d
    WHERE d.dept_id = s.dept_id
);
```

---

## 29. Joins

Joins are one of the most important SQL topics.

They combine rows from multiple tables based on a related column.

Assume two tables:

### `students`
| student_id | name  | dept_id |
|------------|-------|---------|
| 1          | Alina | 10      |
| 2          | Ravi  | 20      |

### `departments`
| dept_id | dept_name |
|---------|-----------|
| 10      | CSE       |
| 20      | ECE       |

---

### 1. INNER JOIN
Returns matching rows from both tables.

```sql
SELECT s.name, d.dept_name
FROM students s
INNER JOIN departments d
ON s.dept_id = d.dept_id;
```

---

### 2. LEFT JOIN
Returns all rows from left table and matching rows from right table.

```sql
SELECT s.name, d.dept_name
FROM students s
LEFT JOIN departments d
ON s.dept_id = d.dept_id;
```

---

### 3. RIGHT JOIN
Returns all rows from right table and matching rows from left table.

```sql
SELECT s.name, d.dept_name
FROM students s
RIGHT JOIN departments d
ON s.dept_id = d.dept_id;
```

---

### 4. FULL OUTER JOIN
Returns all rows from both tables.

```sql
SELECT s.name, d.dept_name
FROM students s
FULL OUTER JOIN departments d
ON s.dept_id = d.dept_id;
```

> Note: Some systems like MySQL do not directly support `FULL OUTER JOIN`.

---

### Real-life example
In hospital management:
- `appointments` table stores `doctor_id`
- `doctors` table stores doctor details

You use join to show appointment plus doctor name.

---

## 30. Self Join

A self join is when a table joins with itself.

### Example
Employee table with manager relationship:

| emp_id | name  | manager_id |
|--------|-------|------------|
| 1      | Asha  | NULL       |
| 2      | Ravi  | 1          |
| 3      | Meera | 1          |

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.emp_id;
```

### Real-life example
Used for:
- employee-manager hierarchy
- parent-child relationships
- category-subcategory structure

---

## 31. Set Operations

Used to combine results of multiple queries.

### UNION
Combines results and removes duplicates.

```sql
SELECT city FROM customers
UNION
SELECT city FROM suppliers;
```

### UNION ALL
Combines results and keeps duplicates.

```sql
SELECT city FROM customers
UNION ALL
SELECT city FROM suppliers;
```

### INTERSECT
Returns common rows.

```sql
SELECT city FROM customers
INTERSECT
SELECT city FROM suppliers;
```

### EXCEPT / MINUS
Returns rows from first query not in second.

```sql
SELECT city FROM customers
EXCEPT
SELECT city FROM suppliers;
```

---

## 32. Subqueries

A subquery is a query inside another query.

### Example
Find students older than average age:
```sql
SELECT *
FROM students
WHERE age > (
    SELECT AVG(age) FROM students
);
```

### Example
Find employees with highest salary:
```sql
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary) FROM employees
);
```

---

## 33. Correlated Subqueries

A correlated subquery depends on the outer query.

### Example
Find employees earning more than average salary in their department:
```sql
SELECT e1.name, e1.salary, e1.dept_id
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.dept_id = e1.dept_id
);
```

### Why important
Common in interview questions and reporting logic.

---

## 34. Views

A view is a virtual table based on a query.

### Create view
```sql
CREATE VIEW cse_students AS
SELECT student_id, name, age
FROM students
WHERE department = 'CSE';
```

### Use view
```sql
SELECT * FROM cse_students;
```

### Why use views?
- simplify complex queries
- improve readability
- provide security by hiding some columns

---

## 35. Indexes

Indexes improve query performance.

### Create index
```sql
CREATE INDEX idx_student_name
ON students(name);
```

### Why use indexes?
They make searching faster.

### Downside
- takes extra storage
- slows down insert/update/delete slightly

### Real-life example
If you often search employees by email, indexing email helps.

---

## 36. SQL Functions

SQL has built-in functions for:
- text
- numbers
- dates
- null handling
- conditional logic

Examples:
- `UPPER()`
- `LOWER()`
- `LENGTH()`
- `ROUND()`
- `NOW()`
- `COALESCE()`

---

## 37. String Functions

### Common string functions
```sql
SELECT UPPER(name) FROM students;
SELECT LOWER(name) FROM students;
SELECT LENGTH(name) FROM students;
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
SELECT SUBSTRING(name, 1, 3) FROM students;
SELECT TRIM(name) FROM students;
```

### Real-life example
Convert emails to lowercase for consistency:
```sql
SELECT LOWER(email) FROM users;
```

---

## 38. Date and Time Functions

Functions vary by database, but common ideas remain same.

### Examples
```sql
SELECT CURRENT_DATE;
SELECT CURRENT_TIME;
SELECT NOW();
```

### Extract year or month
```sql
SELECT YEAR(joined_date) FROM employees;
SELECT MONTH(joined_date) FROM employees;
```

### Real-life example
Find orders placed today:
```sql
SELECT * FROM orders
WHERE order_date = CURRENT_DATE;
```

---

## 39. Numeric Functions

### Examples
```sql
SELECT ROUND(123.456, 2);
SELECT CEIL(12.3);
SELECT FLOOR(12.9);
SELECT ABS(-25);
SELECT MOD(10, 3);
```

### Use cases
- rounding marks
- financial reporting
- price calculations

---

## 40. CASE Statement

`CASE` is used for conditional logic inside SQL.

### Example
```sql
SELECT name, marks,
CASE
    WHEN marks >= 90 THEN 'A+'
    WHEN marks >= 75 THEN 'A'
    WHEN marks >= 50 THEN 'Pass'
    ELSE 'Fail'
END AS grade
FROM results;
```

### Real-life example
Categorize salaries:
```sql
SELECT name, salary,
CASE
    WHEN salary < 30000 THEN 'Low'
    WHEN salary BETWEEN 30000 AND 70000 THEN 'Medium'
    ELSE 'High'
END AS salary_band
FROM employees;
```

---

## 41. Stored Procedures

A stored procedure is a saved block of SQL statements.

### Example idea
A procedure to insert a patient record and create default billing entry.

### Syntax varies by database

Example in MySQL style:
```sql
DELIMITER //

CREATE PROCEDURE GetAllStudents()
BEGIN
    SELECT * FROM students;
END //

DELIMITER ;
```

### Call procedure
```sql
CALL GetAllStudents();
```

### Why use procedures?
- reuse logic
- centralize business rules
- reduce repeated SQL

---

## 42. Triggers

A trigger automatically runs when certain events happen on a table.

### Events
- `INSERT`
- `UPDATE`
- `DELETE`

### Example idea
Whenever a new employee is inserted, add a log entry.

Example structure:
```sql
CREATE TRIGGER after_student_insert
AFTER INSERT ON students
FOR EACH ROW
INSERT INTO student_log(student_id, action_type)
VALUES (NEW.student_id, 'INSERT');
```

### Real-life example
Used for:
- audit logs
- automatic timestamps
- stock update after sale

---

## 43. Transactions

A transaction is a group of SQL operations treated as one unit.

### Example
Bank transfer:
1. subtract money from account A
2. add money to account B

Both must happen together.

### Commands
- `BEGIN` / `START TRANSACTION`
- `COMMIT`
- `ROLLBACK`
- `SAVEPOINT`

### Example
```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 1000
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 1000
WHERE account_id = 2;

COMMIT;
```

### Rollback example
```sql
ROLLBACK;
```

---

## 44. ACID Properties

Transactions follow ACID principles.

### 1. Atomicity
Either all operations happen or none happen.

### 2. Consistency
Database remains valid before and after transaction.

### 3. Isolation
Transactions should not interfere incorrectly with each other.

### 4. Durability
Once committed, data stays saved even after crash.

### Real-life example
In online payment, money should not disappear halfway.

---

## 45. Normalization

Normalization is the process of organizing data to reduce redundancy.

### Why normalize?
- avoid duplicate data
- improve consistency
- make updates easier

### Example of bad design
A student table stores:
- student details
- department name
- hod name
- course name

This causes repetition.

### Better design
Split into separate tables:
- students
- departments
- courses

---

### 1NF – First Normal Form
- each column should contain atomic values
- no repeating groups

### Bad example
| student_id | phones         |
|------------|----------------|
| 1          | 9876, 9123     |

### Better
Separate phone records or separate rows.

---

### 2NF – Second Normal Form
- must be in 1NF
- no partial dependency on part of composite key

### Idea
If table has composite key, non-key columns must depend on the whole key.

---

### 3NF – Third Normal Form
- must be in 2NF
- no transitive dependency

Example:
If `student_id -> dept_id` and `dept_id -> dept_name`, then `dept_name` should be in department table, not student table.

---

## 46. Denormalization

Denormalization is the opposite of normalization.

It intentionally adds redundancy for:
- faster queries
- reporting
- analytics

### Use case
In dashboards, sometimes combined tables are kept for speed.

### Trade-off
- faster reads
- more storage
- harder updates

---

## 47. Common SQL Commands for Projects

### Show all records
```sql
SELECT * FROM patients;
```

### Search by ID
```sql
SELECT * FROM patients
WHERE patient_id = 101;
```

### Search by keyword
```sql
SELECT * FROM doctors
WHERE name LIKE '%John%';
```

### Count records
```sql
SELECT COUNT(*) FROM appointments;
```

### Total billing amount
```sql
SELECT SUM(total_amount) FROM bills;
```

### Most recent entries
```sql
SELECT * FROM appointments
ORDER BY appointment_date DESC
LIMIT 5;
```

### Join-based report
```sql
SELECT a.appointment_id, p.patient_name, d.doctor_name
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;
```

---

## 48. SQL in Real-Life Projects

### 1. Hospital Management System
Tables:
- patients
- doctors
- appointments
- bills

Queries:
- today’s appointments
- patient billing summary
- doctor-wise appointments

---

### 2. College Management System
Tables:
- students
- departments
- marks
- attendance

Queries:
- average marks per subject
- students above class average
- attendance shortage list

---

### 3. E-Commerce Project
Tables:
- customers
- products
- orders
- payments

Queries:
- best-selling product
- revenue by month
- out-of-stock items

---

### 4. Job Portal
Tables:
- users
- resumes
- jobs
- applications

Queries:
- jobs applied by candidate
- number of applicants per job
- latest job postings

---

## 49. Common Interview Questions

### Q1. What is SQL?

SQL is a language used to create, manage, and query relational databases.

---

### Q2. Difference between DBMS and RDBMS?

- DBMS stores data, not always relational
- RDBMS stores data in related tables using keys

---

### Q3. What is a primary key?

A primary key uniquely identifies each row in a table and cannot be null.

---

### Q4. What is a foreign key?

A foreign key is a column that refers to the primary key of another table and helps create relationships.

---

### Q5. Difference between WHERE and HAVING?

- `WHERE` filters rows before grouping
- `HAVING` filters groups after `GROUP BY`

---

### Q6. Difference between DELETE, TRUNCATE, and DROP?

- `DELETE` removes rows, can use `WHERE`
- `TRUNCATE` removes all rows, keeps structure
- `DROP` removes the whole table

---

### Q7. What is a join?

A join combines data from two or more tables using related columns.

---

### Q8. Difference between INNER JOIN and LEFT JOIN?

- `INNER JOIN` returns only matching rows
- `LEFT JOIN` returns all rows from left table and matching rows from right table

---

### Q9. What is normalization?

Normalization is organizing data to reduce redundancy and improve consistency.

---

### Q10. What is an index?

An index improves search speed on a table but may slow inserts/updates.

---

### Q11. What is a view?

A view is a virtual table created from a query.

---

### Q12. What is a transaction?

A transaction is a group of operations executed as one unit.

---

### Q13. What does NULL mean?

`NULL` means missing, unknown, or not available value.

---

### Q14. What is the difference between CHAR and VARCHAR?

- `CHAR` is fixed length
- `VARCHAR` is variable length

---

### Q15. What is the difference between UNION and UNION ALL?

- `UNION` removes duplicates
- `UNION ALL` keeps duplicates

---

## 50. Quick Revision Sheet

### SQL in one paragraph

SQL is the standard language used to manage and query relational databases. It helps us create tables, store records, retrieve data, update values, delete rows, and connect related tables using joins. SQL is widely used in software development, backend systems, data analysis, dashboards, and almost every real-world application involving structured data.

---

### Core topics
- databases
- tables
- rows and columns
- data types
- constraints
- CRUD operations
- joins
- subqueries
- grouping
- transactions

---

### Most important commands
- `CREATE`
- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`
- `ALTER`
- `DROP`
- `TRUNCATE`

---

### Most important clauses
- `WHERE`
- `ORDER BY`
- `GROUP BY`
- `HAVING`
- `LIMIT`

---

### Most important concepts
- primary key
- foreign key
- joins
- normalization
- indexes
- views
- transactions
- ACID properties

---

### Aggregate functions
- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

---

### Join summary
- `INNER JOIN` → matching rows only
- `LEFT JOIN` → all left rows + matching right rows
- `RIGHT JOIN` → all right rows + matching left rows
- `FULL OUTER JOIN` → all rows from both tables

---

### Important interview lines
- SQL is used to manage relational databases.
- Primary key uniquely identifies a record.
- Foreign key creates relationship between tables.
- `WHERE` filters rows; `HAVING` filters groups.
- Joins are used to combine related data.
- Normalization reduces redundancy.
- Indexes improve query speed.
- Transactions ensure reliable data operations.

---

## ✅ Final 10 Things to Remember

1. SQL is the language for relational databases.
2. Tables store data in rows and columns.
3. `SELECT` fetches data.
4. `INSERT` adds data.
5. `UPDATE` modifies data.
6. `DELETE` removes data.
7. Primary key uniquely identifies records.
8. Foreign key links tables.
9. Joins combine data from multiple tables.
10. Transactions protect important operations.

---

## 🎯 One-Minute Interview Answer

**What is SQL?**

SQL stands for Structured Query Language. It is used to create, manage, and query relational databases. With SQL, we can create tables, insert records, update data, delete data, and retrieve information using queries. It also allows us to connect related tables using joins and maintain data integrity using keys and constraints. SQL is widely used in backend development, data analysis, reporting, and real-world software systems such as banking, hospitals, e-commerce, and college management systems.

---

## 📌 Best Way to Study This

Read in this order:
1. What SQL is
2. Databases, tables, rows, columns
3. Data types and constraints
4. CRUD operations
5. Filtering and sorting
6. Aggregate functions and grouping
7. Joins
8. Subqueries
9. Transactions and ACID
10. Normalization and interview questions





## 📖 License

This repository is for learning, revision, and interview preparation.
