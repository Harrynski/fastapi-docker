CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            join_date DATE DEFAULT CURRENT_DATE
        );

INSERT INTO customers (first_name, last_name, email) VALUES ('Juan', 'Perez', 'juan.perez@gmail.com')

select * from customers
