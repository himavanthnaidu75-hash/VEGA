from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from .api.router import api_router
from .core.database import init_db
from .engine.orchestrator import TradingOrchestrator
from .engine.scheduler import VegaScheduler
import asyncio
import json

app = FastAPI(title="VEGA 2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Should be tightened in production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

orchestrator = TradingOrchestrator()
scheduler = VegaScheduler(orchestrator)

@app.on_event("startup")
async def startup_event():
    init_db()
    scheduler.start()

# WebSocket Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Send periodic updates
            data = {
                "status": "RUNNING",
                "pnl": 0.0, # Get from risk manager
                "positions": len(orchestrator.broker.get_positions())
            }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
