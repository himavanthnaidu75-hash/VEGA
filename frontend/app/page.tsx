"use client";
import { useState, useEffect } from "react";
import QuantNebula from "@/components/QuantNebula";
import { Activity, ShieldAlert, TrendingUp, DollarSign, List, BarChart3 } from "lucide-react";
import KillSwitch from "@/components/KillSwitch";

export default function Home() {
  const [status, setStatus] = useState({ running: false, active_trades: 0, balance: { balance: 0 } });
  const [sentiment, setSentiment] = useState({ sentiment: "NEUTRAL", headlines: [] });

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const res = await fetch("http://localhost:8000/api/status");
        const data = await res.json();
        setStatus(data);
      } catch (e) {}
    };
    const interval = setInterval(fetchStatus, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleToggle = async () => {
    const endpoint = status.running ? "stop" : "start";
    await fetch(`http://localhost:8000/api/${endpoint}`, { method: "POST" });
  };

  return (
    <main className="min-h-screen p-8 font-mono relative overflow-hidden text-black selection:bg-gold/30">
      <QuantNebula />

      {/* Header */}
      <div className="flex justify-between items-center mb-12 border-b border-gray-100 pb-4">
        <div>
          <h1 className="text-4xl font-bold tracking-tighter flex items-center gap-3">
            VEGA <span className="text-xs bg-gold text-white px-2 py-1 rounded">V1.0</span>
          </h1>
          <p className="text-xs text-gray-400 uppercase tracking-widest mt-1">
            Volatility Edge & Growth Automaton
          </p>
        </div>

        <div className="flex gap-8 items-center">
          <div className="text-right">
            <p className="text-[10px] text-gray-400 uppercase">System Heartbeat</p>
            <p className={`text-sm font-bold ${status.running ? "text-emerald-500" : "text-amber-500"}`}>
              {status.running ? "NOMINAL" : "STANDBY"}
            </p>
          </div>
          <button
            onClick={handleToggle}
            className={`px-6 py-2 border-2 ${status.running ? "border-red-500 text-red-500 hover:bg-red-50" : "border-blue-500 text-blue-500 hover:bg-blue-50"} transition-all font-bold text-xs uppercase tracking-widest`}
          >
            {status.running ? "TERMINATE" : "INITIATE"}
          </button>
        </div>
      </div>

      {/* Grid Layout */}
      <div className="grid grid-cols-12 gap-6">
        {/* Market Pulse */}
        <div className="col-span-3 bg-white/60 backdrop-blur-xl border border-gray-100 p-6 shadow-sm rounded-sm">
          <h3 className="text-[10px] text-gray-400 uppercase flex items-center gap-2 mb-4 font-bold">
            <Activity size={14} className="text-blue-500" /> Market Pulse
          </h3>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-xs font-medium">NIFTY 50</span>
              <span className="text-xs font-bold tabular-nums">22,456.70</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-xs font-medium text-gray-400">VIX</span>
              <span className="text-xs font-bold text-amber-500 tabular-nums">15.24</span>
            </div>
          </div>
        </div>

        {/* Account Data */}
        <div className="col-span-3 bg-white/60 backdrop-blur-xl border border-gray-100 p-6 shadow-sm rounded-sm">
          <h3 className="text-[10px] text-gray-400 uppercase flex items-center gap-2 mb-4 font-bold">
            <DollarSign size={14} className="text-gold" /> Account
          </h3>
          <p className="text-2xl font-bold tabular-nums">
            ₹{status.balance.balance?.toLocaleString() || "0"}
          </p>
          <div className="flex justify-between mt-2">
             <span className="text-[10px] text-gray-400 uppercase">Margin Used</span>
             <span className="text-[10px] font-bold tabular-nums">₹0</span>
          </div>
        </div>

        {/* Sentiment Strip */}
        <div className="col-span-6 bg-white/60 backdrop-blur-xl border border-gray-100 p-6 shadow-sm rounded-sm">
          <h3 className="text-[10px] text-gray-400 uppercase flex items-center gap-2 mb-4 font-bold">
            <List size={14} className="text-blue-400" /> Sentiment Analysis
          </h3>
          <div className="flex items-center gap-4">
             <div className="px-3 py-1 bg-gray-50 border border-gray-100 text-[10px] font-bold">BULLISH</div>
             <p className="text-[10px] text-gray-500 truncate italic">"HDFC Bank targets raised by institutional analysts..."</p>
          </div>
        </div>

        {/* Signal Feed */}
        <div className="col-span-4 bg-white/60 backdrop-blur-xl border border-gray-100 p-6 shadow-sm rounded-sm h-[400px]">
          <h3 className="text-[10px] text-gray-400 uppercase flex items-center gap-2 mb-4 font-bold">
            <TrendingUp size={14} className="text-gold" /> Signal Engine
          </h3>
          <div className="text-[10px] space-y-3 font-mono overflow-y-auto h-full pr-2 custom-scrollbar">
            <p className="text-blue-500">[09:15:02] INITIALIZING ICT SCANNER...</p>
            <p className="text-gold">[09:15:15] RELIANCE.NS - FVG DETECTED (BULLISH)</p>
            <p className="text-gray-400">[09:16:00] WAITING FOR LIQUIDITY SWEEP AT PDL...</p>
            <p className="text-gray-400">[09:18:22] INTRADAY PHASE: ACCUMULATION</p>
          </div>
        </div>

        {/* Active Trades */}
        <div className="col-span-8 bg-white/60 backdrop-blur-xl border border-gray-100 p-6 shadow-sm rounded-sm h-[400px]">
          <h3 className="text-[10px] text-gray-400 uppercase flex items-center gap-2 mb-6 font-bold">
            <ShieldAlert size={14} className="text-red-500" /> Active Deployments
          </h3>
          <div className="flex flex-col items-center justify-center h-full opacity-20">
             <ShieldAlert size={48} className="mb-4" />
             <p className="text-[10px] uppercase tracking-widest">No active market exposure</p>
          </div>
        </div>

        {/* Ledger */}
        <div className="col-span-12 bg-white/60 backdrop-blur-xl border border-gray-100 p-6 shadow-sm rounded-sm">
          <h3 className="text-[10px] text-gray-400 uppercase flex items-center gap-2 mb-4 font-bold">
            <BarChart3 size={14} /> Today's Ledger
          </h3>
          <div className="grid grid-cols-4 gap-4">
             <div className="border-l-2 border-gold pl-4">
                <p className="text-[10px] text-gray-400 uppercase">Win Rate</p>
                <p className="text-lg font-bold">-- %</p>
             </div>
             <div className="border-l-2 border-emerald-500 pl-4">
                <p className="text-[10px] text-gray-400 uppercase">Realized P&L</p>
                <p className="text-lg font-bold">₹0.00</p>
             </div>
          </div>
        </div>
      </div>

      <KillSwitch onTerminate={handleToggle} />

      <style jsx global>{`
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
        body {
          background: white;
          color: black;
          font-family: 'JetBrains Mono', monospace;
        }
        .bg-gold { background-color: #FFD700; }
        .text-gold { color: #FFD700; }
        .custom-scrollbar::-webkit-scrollbar { width: 2px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #FFD700; }
      `}</style>
    </main>
  );
}
