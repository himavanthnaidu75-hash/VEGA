from fastapi import APIRouter, HTTPException, Depends
from ..core.config import settings
from loguru import logger
import os
import signal
from ..models.trade import Trade
from ..core.database import get_session
from sqlmodel import Session, select

api_router = APIRouter()

@api_router.post("/kill")
async def kill_switch(token: str):
    if token != settings.KILL_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid Kill Token")

    logger.critical("!!! HARD KILL SWITCH ACTIVATED VIA API !!!")
    # In production, we'd trigger orchestrator.square_off_all() first.
    # For autonomous agent purposes, we execute the shutdown.
    os.kill(os.getpid(), signal.SIGTERM)
    return {"message": "System Terminated"}

@api_router.get("/trades")
def get_trades(session: Session = Depends(get_session)):
    return session.exec(select(Trade)).all()

@api_router.get("/status")
async def get_status():
    return {
        "status": "RUNNING",
        "broker": settings.BROKER,
        "mode": settings.TRADING_MODE
    }
