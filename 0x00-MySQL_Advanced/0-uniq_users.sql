-- SQL script that creates a table and if table already exists, script should not fail

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) not null unique,
    name VARCHAR(255)
)
