# TradeLens 🏦 ™
**Backend API for Portfolio Tracking, Virtual Trading & Technical Signal Generation**

# PROJECT OVERVIEW
TradeLens is a backend system built with **FastAPI & Firebase Firestore**, designed for beginner and intermediate investors to simulate portfolio allocation, add tickers with weights, and generate basic BUY/SELL/HOLD trading signals using real market data.

Originally built with MySQL, the system was migrated to Firestore for easier development, rapid cloud syncing, and NoSQL document storage.

This backend is fully API-driven, supports JSON input/output, and includes live Swagger Docs + Postman integration for testing.

# KEY FEATURES ✨
* **User Management**
    - Create user profiles with risk tolerance + investment horizon.
    - Prevent duplicate accounts based on email.
    - Retrieve and store user data in Firestore securely

* **Portfolio Tracking**
    - Create portfolios linked to Firestore user IDs
    - Add stocks/tickers with percentage allocation
    - Retrieve a portfolio including all embedded tickers

* **Trading Signals (Live Market Prices)**
    - Uses yfinance + pandas to generate signals based on SMA crossover:

    ``` 
    Indicator               Logic

    BUY 📈	                SMA20 > SMA50
    SELL 📉	                SMA20 < SMA50
    HOLD 🟡	                Otherwise
    ```


# TECHNICAL STACK 🏗
   - Backend Framework: FastAPI
   - Database: Google Firestore (NoSQL)
   - Market Data: yfinance (Yahoo Finance API)
   - Models/Schemas: Pydantic
   - Deployment Ready: vicorn & Firestore Cloud
   - Tools Used: Postman, SwaggerUI, Python Virtualenv

# HOW TO RUN LOCALLY 🚀 
1. Clone the repo
2. ```
    cd backend
    ```
3. Create & activate virtual environment
    - python3 -m venv venv
    - source venv/bin/activate
4. Install dependencies
    - pip install -r requirements.txt
5. Add Firestore credentials (Place your service key here — but DO NOT COMMIT IT)
    - backend/app/credentials/firebase-key.json
6. Run the API server
    - uvicorn app.main:app --reload

# SECURITY & ENV SETUP 🔒 
    Never push credentials — add to .gitignore
    ``` 
    app/credentials/firebase-key.json
    *.env
    ```

# Contributors 👤
- Kelvin Ihezue, Sathya Gopinath & Surya Gopinath.


