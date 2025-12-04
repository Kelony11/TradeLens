# app/schemas.py
from typing import List, Optional
from pydantic import BaseModel

# ---------- Users ----------

class UserCreate(BaseModel):
    email: Optional[str] = None
    risk_tolerance: str
    horizon_years: int


class UserOut(BaseModel):
    user_id: str           # <- was int
    email: Optional[str]
    risk_tolerance: str
    horizon_years: int


# ---------- Portfolios ----------

class PortfolioCreate(BaseModel):
    user_id: str           # <- was int
    name: str


class PortfolioOut(BaseModel):
    portfolio_id: str      # <- was int
    user_id: str           # <- was int
    name: str


# ---------- Tickers ----------

class TickerAdd(BaseModel):
    portfolio_id: str      # <- was int
    symbol: str
    weight: float


class PortfolioTickerOut(BaseModel):
    ticker_id: str         # new field if you want the id
    symbol: str
    weight: float


class PortfolioDetailOut(BaseModel):
    portfolio_id: str
    user_id: str
    name: str
    tickers: List[PortfolioTickerOut]


# ---------- Signals ----------

class SignalRequest(BaseModel):
    symbols: List[str]


class SignalOut(BaseModel):
    symbol: str
    action: str
