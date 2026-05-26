#!/bin/bash
echo "Launching VEGA (Volatility Edge & Growth Automaton)..."

# Start Backend
cd backend
python3 main.py > ../vega_backend.log 2>&1 &
BACKEND_PID=$!

# Start Frontend
cd ../frontend
npm run dev > ../vega_frontend.log 2>&1 &
FRONTEND_PID=$!

echo "VEGA Online."
echo "Terminal: http://localhost:3000"
echo "API: http://localhost:8000"
echo "To stop: kill $BACKEND_PID $FRONTEND_PID"

wait
