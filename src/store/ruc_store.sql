CREATE DATABASE IF NOT EXISTS ruc_store;
USE ruc_store;

DROP TABLE IF EXISTS `User`;
CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL DEFAULT '私密',
    email VARCHAR(120) NOT NULL,
    table_name VARCHAR(20) NOT NULL,
    table_id INT NOT NULL
);


DROP TABLE IF EXISTS `Customer`;
CREATE TABLE Customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(60) NOT NULL,
    consignee VARCHAR(20) NOT NULL DEFAULT 'null',
    address VARCHAR(40) NOT NULL DEFAULT 'null',
    telephone VARCHAR(20) NOT NULL DEFAULT 'null'
);


DROP TABLE IF EXISTS `Supplier`;
CREATE TABLE Supplier (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(60) NOT NULL,
    shipper VARCHAR(40) NOT NULL DEFAULT 'null',
    address VARCHAR(40) NOT NULL DEFAULT 'null',
    telephone VARCHAR(20) NOT NULL DEFAULT 'null'
);


DROP TABLE IF EXISTS `Product`;
CREATE TABLE `Product` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(40) NOT NULL DEFAULT 'null',
    `price` FLOAT NOT NULL DEFAULT 0.00,
    `count` INT NOT NULL DEFAULT 0,
    `supplier_id` INT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY (Supplier_id) REFERENCES Supplier (id)
);


DROP TABLE IF EXISTS `Order`;
CREATE TABLE `Order` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status INT NOT NULL DEFAULT 0,
    start_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_price FLOAT NOT NULL DEFAULT 0.00,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer (id)
);


DROP TABLE IF EXISTS `OrderDetail`;
CREATE TABLE OrderDetail (
    id INT AUTO_INCREMENT PRIMARY KEY,
    count INT NOT NULL,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES `Order` (id),
    FOREIGN KEY (product_id) REFERENCES Product (id)
);
