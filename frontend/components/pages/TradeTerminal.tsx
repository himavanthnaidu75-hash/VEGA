"use client";
import React from "react";
import { motion } from "framer-motion";
import { Zap, ShieldCheck, Target, TrendingUp } from "lucide-react";

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
    symbol: "NIFTY_BANK",
    price: "47,890.00",
    side: "BEARISH",
    confirmations: 1,
    entry: "48,000.00",
    sl: "48,200.00",
    tp: "47,400.00",
  },
];

const newsFeed = [
  { title: "Institutional accumulation detected on NIFTY Bank", time: "12:04", type: "ALPHA" },
  { title: "RBI Policy: Hawkish stance maintains market stability", time: "11:45", type: "MACRO" },
  { title: "HDFC Bank liquidity sweep confirmed at PDL", time: "11:20", type: "SIGNAL" },
];

export default function TradeTerminal() {
  return (
    <div className="grid grid-cols-12 gap-12">
      {/* Left Scanner */}
      <div className="col-span-8 space-y-10">
        <header className="flex justify-between items-end">
          <div className="space-y-1">
            <h2 className="text-4xl font-bold tracking-tighter text-platinum">TERMINAL</h2>
            <p className="text-[10px] text-gold tracking-[0.4em] font-bold uppercase">Institutional Scanning Engine</p>
          </div>
          <div className="flex gap-10">
             <div className="text-right">
                <p className="text-[8px] text-text-secondary uppercase tracking-widest mb-1">Active Scans</p>
                <p className="font-data text-xs text-platinum">50 Assets</p>
             </div>
             <div className="text-right">
                <p className="text-[8px] text-text-secondary uppercase tracking-widest mb-1">Total Alpha</p>
                <p className="font-data text-xs text-profit">+2.4% Today</p>
             </div>
          </div>
        </header>

        <div className="grid grid-cols-2 gap-8">
          {opportunities.map((opt, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.1 }}
              whileHover={{ y: -5, scale: 1.02 }}
              className={`glass-lux p-8 rounded-sm relative group cursor-pointer transition-all duration-500 ${
                opt.confirmations === 4 ? "border-gold/50 shadow-[0_0_40px_rgba(212,175,55,0.1)]" : ""
              }`}
            >
              <div className="flex justify-between items-start mb-8">
                <div>
                  <h3 className="text-xl font-bold tracking-tight text-platinum">{opt.symbol}</h3>
                  <span className="font-data text-[10px] text-text-secondary mt-1 block">QUOTE: ₹{opt.price}</span>
                </div>
                <div className={`px-4 py-1 text-[9px] font-bold tracking-[0.2em] rounded-full border ${
                  opt.side === "BULLISH" ? "border-profit/30 text-profit bg-profit/5" : "border-loss/30 text-loss bg-loss/5"
                }`}>
                  {opt.side}
                </div>
              </div>

              {/* Progress Tracker */}
              <div className="space-y-3 mb-10">
                <div className="flex justify-between text-[8px] text-text-secondary uppercase tracking-widest font-bold">
                  <span>Confirmations</span>
                  <span>{opt.confirmations}/4 Verified</span>
                </div>
                <div className="flex gap-2">
                  {[1, 2, 3, 4].map((step) => (
                    <div key={step} className="flex-1 h-[2px] bg-white/5 relative overflow-hidden">
                      {step <= opt.confirmations && (
                        <motion.div
                          initial={{ width: 0 }}
                          animate={{ width: "100%" }}
                          className="absolute inset-0 bg-gold shadow-[0_0_10px_#D4AF37]"
                        />
                      )}
                    </div>
                  ))}
                </div>
              </div>

              {/* Execution Map */}
              <div className="grid grid-cols-3 gap-6 pt-6 border-t border-white/5">
                <div>
                  <p className="text-[8px] text-text-secondary uppercase mb-2">Entry Target</p>
                  <p className="font-data text-xs text-platinum">₹{opt.entry}</p>
                </div>
                <div>
                  <p className="text-[8px] text-text-secondary uppercase mb-2 text-center">Stop (Hard)</p>
                  <p className="font-data text-xs text-loss text-center">₹{opt.sl}</p>
                </div>
                <div>
                  <p className="text-[8px] text-text-secondary uppercase mb-2 text-right">TP (Max)</p>
                  <p className="font-data text-xs text-profit text-right">₹{opt.tp}</p>
                </div>
              </div>

              {opt.confirmations === 4 && (
                <motion.div
                  animate={{ opacity: [0, 0.3, 0] }}
                  transition={{ repeat: Infinity, duration: 2 }}
                  className="absolute inset-0 bg-gold pointer-events-none rounded-sm"
                />
              )}
            </motion.div>
          ))}
        </div>
      </div>

      {/* Right Intelligence Feed */}
      <div className="col-span-4 space-y-8">
        <div className="glass-lux p-6 rounded-sm border-l-4 border-gold">
           <div className="flex items-center gap-3 mb-3">
              <ShieldCheck size={16} className="text-gold" />
              <h4 className="text-[10px] font-bold text-platinum uppercase tracking-[0.2em]">Institutional Sentinel</h4>
           </div>
           <p className="text-[10px] text-text-secondary leading-relaxed font-light">
             Scanning NSE Order Flow. Detection of Large-Scale Liquidity Sweeps currently active on <span className="text-gold font-bold">RELIANCE</span>.
           </p>
        </div>

        <div className="glass-lux p-8 rounded-sm h-[580px] flex flex-col">
           <h3 className="text-[10px] text-gold font-bold uppercase tracking-[0.3em] mb-10 flex items-center gap-2">
              <TrendingUp size={16} /> Market Intelligence
           </h3>

           <div className="space-y-10 overflow-y-auto pr-3 custom-scrollbar">
              {newsFeed.map((item, i) => (
                <div key={i} className="relative pl-6 space-y-2 border-l border-white/5 pb-2">
                   <div className="absolute left-[-4.5px] top-0 w-2 h-2 rounded-full bg-gold border-2 border-bg-pure" />
                   <div className="flex justify-between items-center text-[9px] font-bold">
                      <span className="text-gold/60 uppercase tracking-widest">{item.type}</span>
                      <span className="font-data text-text-secondary opacity-50">{item.time}</span>
                   </div>
                   <p className="text-xs text-platinum/90 leading-relaxed font-light">{item.title}</p>
                </div>
              ))}
           </div>
        </div>
      </div>
    </div>
  );
}
