-- 1. CRIAÇÃO DO BANCO 
CREATE DATABASE IF NOT EXISTS myDB;
USE myDB;

-- 2. CRIAÇÃO DA TABELA 
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5, 2),
    hire_date DATE
);

-- 3. INSERÇÃO DOS DADOS 
INSERT IGNORE INTO employees (employee_id, first_name, last_name, hourly_pay, hire_date) 
VALUES 
    (1, 'Eugene', 'Krabs', 25.50, '2023-01-02'),
    (2, 'Squidward', 'Tentacles', 15.00, '2023-01-03'),
    (3, 'Spongebob', 'Squarepants', 12.50, '2023-01-04'),
    (4, 'Patrick', 'Star', 12.50, '2023-01-05'),
    (5, 'Sandy', 'Cheeks', 17.25, '2023-01-06'),
    (6, 'Sheldon', 'Plankton', NULL, NULL);

-- 4. CONSULTA PARA CONFERIR
SELECT * FROM employees;
