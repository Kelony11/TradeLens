from typing import List, Optional
from pydantic import BaseModel

# --------------------------
# User Schemas
# --------------------------

class UserCreate(BaseModel):
    email: Optional[str] = None
    risk_tolerance: str
    horizon_years: int


class UserOut(BaseModel):
    user_id: int
    email: Optional[str]
    risk_tolerance: str
    horizon_years: int

    class Config:
        orm_mode = True


# --------------------------
# Portfolio Schemas
# --------------------------

class PortfolioCreate(BaseModel):
    user_id: int
    name: str


class PortfolioOut(BaseModel):
    portfolio_id: int
    user_id: int
    name: str

    class Config:
        orm_mode = True


# --------------------------
# Ticker Schemas
# --------------------------

class TickerAdd(BaseModel):
    portfolio_id: int
    symbol: str
    weight: float


class PortfolioTickerOut(BaseModel):
    symbol: str
    weight: float

    class Config:
        orm_mode = True


class PortfolioDetailOut(BaseModel):
    portfolio_id: int
    user_id: int
    name: str
    tickers: List[PortfolioTickerOut]

    class Config:
        orm_mode = True


# --------------------------
# Signal Engine Schemas
# --------------------------

class SignalRequest(BaseModel):
    symbols: List[str]


class SignalOut(BaseModel):
    symbol: str
    action: str
