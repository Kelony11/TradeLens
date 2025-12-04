# models.py — FIRESTORE VERSION

from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    email: Optional[str]
    risk_tolerance: str
    horizon_years: int

class Portfolio(BaseModel):
    portfolio_id: str
    user_id: str
    name: str

class PortfolioTicker(BaseModel):
    ticker_id: str
    portfolio_id: str
    symbol: str
    weight: float
