from fastapi import APIRouter
from .schemas import SignalRequest, SignalOut
from .indicators import simple_signal

router = APIRouter(
    prefix="/signals",
    tags=["Signals"]
)

# --------------------------
# Generate SMA-based Signals
# --------------------------

@router.post("/generate", response_model=list[SignalOut])
def generate_signals(payload: SignalRequest):
    """
    Generates BUY/SELL/HOLD signals for a list of stock symbols
    using the simple SMA crossover strategy.
    """

    results = []

    for symbol in payload.symbols:
        try:
            action = simple_signal(symbol)
        except Exception:
            action = "ERROR"

        results.append(SignalOut(symbol=symbol, action=action))

    return results
