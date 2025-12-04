# app/routers_portfolios.py

from fastapi import APIRouter, Depends, HTTPException
from google.cloud.firestore import Client

from .database import get_db
from . import crud, schemas

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolios"]
)

# --------------------------
# Create Portfolio
# --------------------------

@router.post("/create", response_model=schemas.PortfolioOut)
def create_portfolio(portfolio: schemas.PortfolioCreate, db: Client = Depends(get_db)):
    """
    Creates a new portfolio for an existing user.
    The user_id must be a valid user_id from the users collection.
    """
    # Check user exists by ID
    user = crud.get_user_by_id(db, portfolio.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_portfolio(db, portfolio)


# --------------------------
# Add Ticker to Portfolio
# --------------------------

@router.post("/add_ticker", response_model=schemas.PortfolioTickerOut)
def add_ticker(ticker: schemas.TickerAdd, db: Client = Depends(get_db)):
    """
    Adds a ticker + weight to an existing portfolio.
    """

    # Optional: check portfolio exists
    doc = db.collection("portfolios").document(ticker.portfolio_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Portfolio not found")

    return crud.add_ticker(db, ticker)


# --------------------------
# Get Portfolio (with tickers)
# --------------------------

@router.get("/{portfolio_id}", response_model=schemas.PortfolioDetailOut)
def get_portfolio(portfolio_id: str, db: Client = Depends(get_db)):
    """
    Returns portfolio metadata plus its list of tickers and weights.
    """

    result = crud.get_portfolio_with_tickers(db, portfolio_id)
    if not result:
        raise HTTPException(status_code=404, detail="Portfolio not found")

    return result
