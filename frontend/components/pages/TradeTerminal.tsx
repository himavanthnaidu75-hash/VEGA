"use client";
import React from "react";
import { motion } from "framer-motion";
import { TrendingUp, AlertCircle, CheckCircle2 } from "lucide-react";

const opportunities = [
  {
    symbol: "RELIANCE.NS",
    price: "2,945.60",
    side: "BULLISH",
    confirmations: 3,
    entry: "2,940.00",
    sl: "2,930.00",
    tp: "2,970.00",
  },
  {
    symbol: "TCS.NS",
    price: "4,120.30",
    side: "BEARISH",
    confirmations: 4,
    entry: "4,125.00",
    sl: "4,150.00",
    tp: "4,050.00",
  },
  {
    symbol: "INFY.NS",
    price: "1,680.15",
    side: "BULLISH",
    confirmations: 2,
    entry: "1,675.00",
    sl: "1,660.00",
    tp: "1,710.00",
  },
  {
    symbol: "BANKNIFTY",
    price: "47,890.00",
    side: "BEARISH",
    confirmations: 1,
    entry: "48,000.00",
    sl: "48,200.00",
    tp: "47,400.00",
  },
];

const news = [
  { title: "RBI maintains repo rate, focus on inflation", time: "10m ago", sentiment: "NEUTRAL" },
  { title: "HDFC Bank Q4 results exceed expectations", time: "25m ago", sentiment: "BULLISH" },
  { title: "Global markets trade weak on inflation fears", time: "45m ago", sentiment: "BEARISH" },
];

export default function TradeTerminal() {
  return (
    <div className="grid grid-cols-12 gap-8">
      {/* Main Terminal */}
      <div className="col-span-8 space-y-8">
        <header className="flex flex-col">
          <h2 className="text-4xl font-light tracking-tighter text-white">TRADE TERMINAL</h2>
          <span className="text-[10px] text-teal-blue tracking-[0.3em] font-bold uppercase mt-1">
            ICT/SMC OPPORTUNITY SCANNER
          </span>
        </header>

        <div className="grid grid-cols-2 gap-6">
          {opportunities.map((opt, i) => (
            <motion.div
              key={i}
              whileHover={{ y: -4, scale: 1.01 }}
              className={`glass-card p-6 rounded-sm relative overflow-hidden transition-all duration-500 ${
                opt.confirmations === 4 ? "border-purple-royal/60 shadow-[0_0_20px_rgba(102,0,204,0.15)]" : ""
              }`}
            >
              {/* Left Glow Border */}
              <div
                className={`absolute left-0 top-0 bottom-0 w-[3px] bg-purple-royal transition-all duration-500 ${
                  opt.confirmations === 4 ? "opacity-100 shadow-[0_0_10px_#6600CC]" : "opacity-30"
                }`}
              />

              <div className="flex justify-between items-start mb-6">
                <div>
                  <h3 className="text-xl font-bold text-white tracking-tight">{opt.symbol}</h3>
                  <p className="font-data text-sm text-text-secondary mt-1 tracking-wider">₹{opt.price}</p>
                </div>
                <div className={`px-3 py-1 rounded-full text-[10px] font-bold tracking-widest ${
                  opt.side === "BULLISH" ? "bg-profit/10 text-profit border border-profit/20" : "bg-loss/10 text-loss border border-loss/20"
                }`}>
                  {opt.side}
                </div>
              </div>

              {/* Confirmation Dots */}
              <div className="flex gap-2 mb-8">
                {[1, 2, 3, 4].map((dot) => (
                  <div
                    key={dot}
                    className={`w-2 h-2 rounded-full transition-all duration-500 ${
                      dot <= opt.confirmations ? "bg-purple-royal shadow-[0_0_8px_#6600CC]" : "bg-white/10"
                    }`}
                  />
                ))}
                <span className="text-[8px] text-text-secondary uppercase ml-2 tracking-widest font-bold">
                  {opt.confirmations}/4 CONFS
                </span>
              </div>

              {/* Data Grid */}
              <div className="grid grid-cols-3 gap-4 border-t border-white/5 pt-4">
                <div>
                  <p className="text-[8px] text-text-secondary uppercase mb-1">Entry</p>
                  <p className="font-data text-xs text-white">₹{opt.entry}</p>
                </div>
                <div>
                  <p className="text-[8px] text-text-secondary uppercase mb-1">Stop Loss</p>
                  <p className="font-data text-xs text-loss">₹{opt.sl}</p>
                </div>
                <div>
                  <p className="text-[8px] text-text-secondary uppercase mb-1">Target</p>
                  <p className="font-data text-xs text-profit">₹{opt.tp}</p>
                </div>
              </div>

              {opt.confirmations === 4 && (
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: [0.1, 0.3, 0.1] }}
                  transition={{ repeat: Infinity, duration: 2 }}
                  className="absolute inset-0 bg-purple-royal pointer-events-none"
                />
              )}
            </motion.div>
          ))}
        </div>
      </div>

      {/* Side Panel */}
      <div className="col-span-4 space-y-6">
        <div className="bg-purple-royal/10 border border-purple-royal/30 p-4 rounded-sm flex items-start gap-4">
          <AlertCircle className="text-purple-royal flex-shrink-0" size={20} />
          <div>
            <h4 className="text-[10px] font-bold text-white uppercase tracking-widest">High Priority Alert</h4>
            <p className="text-[10px] text-text-secondary mt-1">Institutional liquidity sweep detected on TCS. 15M FVG confirmed. Awaiting CISD.</p>
          </div>
        </div>

        <div className="glass-card p-6 rounded-sm h-[600px] flex flex-col">
          <h3 className="text-[10px] text-teal-blue font-bold uppercase tracking-[0.2em] mb-6 flex items-center gap-2">
            <TrendingUp size={14} /> India Live Feed
          </h3>

          <div className="space-y-6 overflow-y-auto pr-2 custom-scrollbar">
            {news.map((n, i) => (
              <div key={i} className="space-y-2 pb-4 border-b border-white/5">
                <div className="flex justify-between items-center">
                  <span className={`text-[8px] font-bold px-2 py-0.5 rounded ${
                    n.sentiment === "BULLISH" ? "bg-profit/10 text-profit" : n.sentiment === "BEARISH" ? "bg-loss/10 text-loss" : "bg-text-secondary/10 text-text-secondary"
                  }`}>
                    {n.sentiment}
                  </span>
                  <span className="text-[8px] text-text-secondary font-data">{n.time}</span>
                </div>
                <p className="text-xs text-white/80 leading-relaxed">{n.title}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
