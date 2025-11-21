-- ===========================================
-- TradeLens Database Setup Script
-- Creates database and all required tables
-- ===========================================

-- Create the database
CREATE DATABASE IF NOT EXISTS tradelens;
USE tradelens;

-- ===========================
-- Users Table
-- ===========================
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    risk_tolerance VARCHAR(20) NOT NULL,
    horizon_years INT NOT NULL
);

-- ===========================
-- Portfolios Table
-- ===========================
CREATE TABLE IF NOT EXISTS portfolios (
    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ===========================
-- Portfolio Tickers Table
-- ===========================
CREATE TABLE IF NOT EXISTS portfolio_tickers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    portfolio_id INT NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    weight FLOAT NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);
