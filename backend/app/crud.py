# app/crud.py — Firestore version

from google.cloud.firestore import Client
from . import schemas
import uuid

# ---------- Users ----------

def create_user(db: Client, user: schemas.UserCreate) -> schemas.UserOut:
    user_id = str(uuid.uuid4())

    data = {
        "user_id": user_id,
        "email": user.email,
        "risk_tolerance": user.risk_tolerance,
        "horizon_years": user.horizon_years,
    }

    db.collection("users").document(user_id).set(data)
    return schemas.UserOut(**data)


def get_user_by_email(db: Client, email: str):
    query = db.collection("users").where("email", "==", email).stream()
    for doc in query:
        return schemas.UserOut(**doc.to_dict())
    return None


def get_user_by_id(db: Client, user_id: str):
    doc = db.collection("users").document(user_id).get()
    if doc.exists:
        return schemas.UserOut(**doc.to_dict())
    return None


# ---------- Portfolios ----------

def create_portfolio(db: Client, portfolio: schemas.PortfolioCreate) -> schemas.PortfolioOut:
    portfolio_id = str(uuid.uuid4())

    data = {
        "portfolio_id": portfolio_id,
        "user_id": portfolio.user_id,
        "name": portfolio.name,
    }

    db.collection("portfolios").document(portfolio_id).set(data)
    return schemas.PortfolioOut(**data)


def add_ticker(db: Client, ticker: schemas.TickerAdd) -> schemas.PortfolioTickerOut:
    ticker_id = str(uuid.uuid4())

    data = {
        "ticker_id": ticker_id,
        "portfolio_id": ticker.portfolio_id,
        "symbol": ticker.symbol,
        "weight": ticker.weight,
    }

    db.collection("portfolio_tickers").document(ticker_id).set(data)
    return schemas.PortfolioTickerOut(**data)


def get_portfolio_with_tickers(db: Client, portfolio_id: str):
    # Get portfolio
    doc = db.collection("portfolios").document(portfolio_id).get()
    if not doc.exists:
        return None

    portfolio_data = doc.to_dict()

    # Get tickers
    ticker_docs = db.collection("portfolio_tickers").where(
        "portfolio_id", "==", portfolio_id
    ).stream()

    tickers = [schemas.PortfolioTickerOut(**t.to_dict()) for t in ticker_docs]

    return {
        "portfolio_id": portfolio_data["portfolio_id"],
        "user_id": portfolio_data["user_id"],
        "name": portfolio_data["name"],
        "tickers": tickers,
    }
