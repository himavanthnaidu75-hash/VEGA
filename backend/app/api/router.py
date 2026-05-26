from fastapi import APIRouter
from ..engine.orchestrator import VegaOrchestrator
import asyncio

router = APIRouter()
orchestrator = VegaOrchestrator()

@router.get("/status")
async def get_status():
    return {
        "running": orchestrator.is_running,
        "active_trades": len(orchestrator.active_trades),
        "balance": orchestrator.broker.get_balance()
    }

@router.post("/start")
async def start_vega():
    if not orchestrator.is_running:
        asyncio.create_task(orchestrator.start())
        return {"message": "VEGA initialization sequence started"}
    return {"message": "VEGA is already running"}

@router.post("/stop")
async def stop_vega():
    orchestrator.stop()
    return {"message": "Kill switch activated"}
