# VEGA 2.0 - Autonomous Quantitative Trading Platform

VEGA 2.0 is a zero-cost, fully autonomous trading system designed for the Indian financial markets.

## Features
- **151 Quantitative Strategies**: Implemented from institutional-grade logic with 200+ mathematical formulas.
- **Multi-Broker Agnostic**: Support for Dhan (Primary), AngelOne, Zerodha (Paid), and Paper Trading.
- **Institutional Logic**: ICT Confirmation Model (Liquidity Sweeps, Order Blocks, FVGs).
- **Hard Kill Switch**: Multi-channel (UI, API, Telegram, Terminal) safety halt system.
- **Zero Cost**: Uses yfinance, NSE public APIs, and RSS feeds to run entirely for free.

## Setup

### Local Deployment
1. Clone the repository.
2. Create a `.env` file using `.env.example`.
3. Install backend dependencies: `pip install -r vega/backend/requirements.txt`.
4. Install frontend dependencies: `cd vega/frontend && npm install`.
5. Start backend: `python vega/backend/app/main.py`.
6. Start frontend: `npm run dev`.

### Railway / Render
1. Connect your GitHub repo.
2. Set environment variables.
3. Use the start script provided.

## Safety
If the **KILL SWITCH** is triggered, the system will:
1. Cancel all orders.
2. Square off all positions.
3. Shut down the server process.
*Manual restart is required via your deployment dashboard.*
