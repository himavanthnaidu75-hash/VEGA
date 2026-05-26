from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.router import router
import uvicorn

app = FastAPI(title="VEGA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"status": "VEGA Online", "mode": "Autonomous"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
