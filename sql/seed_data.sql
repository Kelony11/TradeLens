-- ===========================================
-- TradeLens Sample Seed Data
-- Inserts demo users, portfolios, and tickers
-- ===========================================

USE tradelens;

-- ===========================
-- Sample User
-- ===========================
INSERT INTO users (email, risk_tolerance, horizon_years)
VALUES 
('demo_user@tradelens.com', 'medium', 2);

-- ===========================
-- Sample Portfolio
-- ===========================
INSERT INTO portfolios (user_id, name)
VALUES 
(1, 'Demo Portfolio');

-- ===========================
-- Sample Tickers
-- ===========================
INSERT INTO portfolio_tickers (portfolio_id, symbol, weight)
VALUES 
(1, 'AAPL', 0.30),
(1, 'TSLA', 0.25),
(1, 'MSFT', 0.45);
