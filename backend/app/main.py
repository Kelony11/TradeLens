# app/main.py

from fastapi import FastAPI

from .routers_users import router as users_router
from .routers_portfolios import router as portfolios_router
from .routers_signals import router as signals_router

app = FastAPI(
    title="TradeLens API (Firestore)",
    version="1.0.0",
    description="Backend for TradeLens using Firebase Firestore",
)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "TradeLens Firestore backend is running"}


# Register routers
app.include_router(users_router)
app.include_router(portfolios_router)
app.include_router(signals_router)
