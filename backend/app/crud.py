from sqlalchemy.orm import Session
from . import models, schemas

# --------------------------
# USER CRUD
# --------------------------

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        risk_tolerance=user.risk_tolerance,
        horizon_years=user.horizon_years,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# --------------------------
# PORTFOLIO CRUD
# --------------------------

def create_portfolio(db: Session, portfolio: schemas.PortfolioCreate):
    db_portfolio = models.Portfolio(
        user_id=portfolio.user_id,
        name=portfolio.name,
    )
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio


# --------------------------
# TICKER CRUD
# --------------------------

def add_ticker(db: Session, ticker: schemas.TickerAdd):
    db_ticker = models.PortfolioTicker(
        portfolio_id=ticker.portfolio_id,
        symbol=ticker.symbol.upper(),
        weight=ticker.weight,
    )
    db.add(db_ticker)
    db.commit()
    db.refresh(db_ticker)
    return db_ticker


# --------------------------
# GET PORTFOLIO (WITH TICKERS)
# --------------------------

def get_portfolio_with_tickers(db: Session, portfolio_id: int):
    """
    Returns a Portfolio object including all related tickers.
    """
    return (
        db.query(models.Portfolio)
        .filter(models.Portfolio.portfolio_id == portfolio_id)
        .first()
    )
