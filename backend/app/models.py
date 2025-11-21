from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# --------------------------
# User Table
# --------------------------

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=True)
    risk_tolerance = Column(String(20), nullable=False)
    horizon_years = Column(Integer, nullable=False)

    # Relationship to portfolios
    portfolios = relationship("Portfolio", back_populates="user")


# --------------------------
# Portfolio Table
# --------------------------

class Portfolio(Base):
    __tablename__ = "portfolios"

    portfolio_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String(255), nullable=False)

    # Relationship back to user
    user = relationship("User", back_populates="portfolios")

    # Relationship to tickers (1-to-many)
    tickers = relationship("PortfolioTicker", back_populates="portfolio")


# --------------------------
# Portfolio Ticketers Table
# --------------------------

class PortfolioTicker(Base):
    __tablename__ = "portfolio_tickers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.portfolio_id"))
    symbol = Column(String(10), nullable=False)
    weight = Column(Float, nullable=False)

    # Relationship back to portfolio
    portfolio = relationship("Portfolio", back_populates="tickers")
