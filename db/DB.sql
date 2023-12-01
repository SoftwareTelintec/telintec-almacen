-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS inventory_management;

-- Usar la base de datos
USE inventory_management;

-- Crear tabla de categorías de productos
CREATE TABLE IF NOT EXISTS product_categories (
    id_category INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

-- Crear tabla de productos
CREATE TABLE IF NOT EXISTS products (
    id_product INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    id_category INT,
    FOREIGN KEY (id_category) REFERENCES product_categories(id_category),
    INDEX idx_category (id_category)
);

-- Crear tabla de clientes
CREATE TABLE IF NOT EXISTS customers (
    id_customer INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    INDEX idx_name (name),
    INDEX idx_email (email)
);

-- Crear tabla de dirección de envío de los clientes
CREATE TABLE IF NOT EXISTS customer_addresses (
    id_address INT PRIMARY KEY AUTO_INCREMENT,
    id_customer INT,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    postal_code VARCHAR(20),
    FOREIGN KEY (id_customer) REFERENCES customers(id_customer)
);

-- Crear tabla de proveedores
CREATE TABLE IF NOT EXISTS suppliers (
    id_supplier INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20)
);

-- Crear tabla de órdenes
CREATE TABLE IF NOT EXISTS orders (
    id_order INT PRIMARY KEY AUTO_INCREMENT,
    id_customer INT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    return_status ENUM('pending', 'processing', 'complete') DEFAULT 'pending',
    FOREIGN KEY (id_customer) REFERENCES customers(id_customer),
    INDEX idx_customer (id_customer)
);

-- Crear tabla de detalles de órdenes
CREATE TABLE IF NOT EXISTS order_details (
    id_order_detail INT PRIMARY KEY AUTO_INCREMENT,
    id_order INT,
    id_product INT,
    quantity INT NOT NULL,
    FOREIGN KEY (id_order) REFERENCES orders(id_order),
    FOREIGN KEY (id_product) REFERENCES products(id_product),
    CONSTRAINT unique_order_product UNIQUE (id_order, id_product),
    INDEX idx_order (id_order),
    INDEX idx_product (id_product)
);

-- Crear tabla de detalles de proveedores y productos
CREATE TABLE IF NOT EXISTS supplier_product (
    id_supplier_product INT PRIMARY KEY AUTO_INCREMENT,
    id_supplier INT,
    id_product INT,
    FOREIGN KEY (id_supplier) REFERENCES suppliers(id_supplier),
    FOREIGN KEY (id_product) REFERENCES products(id_product),
    INDEX idx_supplier (id_supplier),
    INDEX idx_product_supplier (id_product)
);
