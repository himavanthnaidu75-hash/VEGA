"use client";
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Radar, ExternalLink, ShieldCheck } from "lucide-react";

const mockPositions = [
  { symbol: "TCS.NS", side: "SELL", qty: 25, entry: "4,125.00", current: "4,120.30", pnl: "+₹117.50", pnlType: "profit", rr: "1:2.4" },
  { symbol: "RELIANCE.NS", side: "BUY", qty: 50, entry: "2,940.00", current: "2,945.60", pnl: "+₹280.00", pnlType: "profit", rr: "1:1.8" },
];

export default function Positions() {
  const [loading, setLoading] = useState(true);
  const [positions, setPositions] = useState<any[]>([]);

  useEffect(() => {
    setTimeout(() => {
      setPositions(mockPositions);
      setLoading(false);
    }, 1500);
  }, []);

  if (loading) {
    return (
      <div className="space-y-8">
        <div className="h-10 w-48 bg-white/5 animate-pulse rounded" />
        <div className="h-[400px] w-full glass-card animate-pulse rounded" />
      </div>
    );
  }

  const isEmpty = positions.length === 0;

  return (
    <div className="space-y-8">
      <header className="flex flex-col">
        <h2 className="text-4xl font-light tracking-tighter text-white">POSITIONS</h2>
        <span className="text-[10px] text-teal-blue tracking-[0.3em] font-bold uppercase mt-1">
          LIVE MARKET EXPOSURE
        </span>
      </header>

      {isEmpty ? (
        <div className="h-[500px] glass-card rounded-sm flex flex-col items-center justify-center relative overflow-hidden">
           <motion.div
             animate={{ scale: [1, 1.2, 1], opacity: [0.3, 0.6, 0.3] }}
             transition={{ repeat: Infinity, duration: 4 }}
             className="w-64 h-64 border border-purple-royal/20 rounded-full flex items-center justify-center"
           >
             <motion.div
               animate={{ scale: [1, 1.2, 1], opacity: [0.1, 0.3, 0.1] }}
               transition={{ repeat: Infinity, duration: 4, delay: 0.5 }}
               className="w-48 h-48 border border-purple-royal/40 rounded-full flex items-center justify-center"
             >
                <Radar className="text-purple-royal" size={48} />
             </motion.div>
           </motion.div>
           <p className="text-[10px] text-purple-royal uppercase tracking-[0.4em] font-bold mt-8 animate-pulse">
             Scanning for signals...
           </p>
        </div>
      ) : (
        <div className="glass-card rounded-sm overflow-hidden">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-white/5 bg-white/[0.02]">
                <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold">Instrument</th>
                <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold">Side</th>
                <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold text-right">Entry</th>
                <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold text-right">Current</th>
                <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold text-right">Unrealized P&L</th>
                <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold text-right">Action</th>
              </tr>
            </thead>
            <tbody>
              {positions.map((pos, i) => (
                <motion.tr
                  key={i}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: i * 0.1 }}
                  className="border-b border-white/5 hover:bg-white/[0.02] transition-all group"
                >
                  <td className="p-6">
                    <div className="flex flex-col">
                      <span className="text-sm font-bold text-white">{pos.symbol}</span>
                      <span className="text-[10px] text-text-secondary font-data">QTY: {pos.qty}</span>
                    </div>
                  </td>
                  <td className="p-6">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded border ${
                      pos.side === "BUY" ? "text-profit border-profit/20 bg-profit/5" : "text-loss border-loss/20 bg-loss/5"
                    }`}>
                      {pos.side}
                    </span>
                  </td>
                  <td className="p-6 text-right font-data text-xs text-white">₹{pos.entry}</td>
                  <td className="p-6 text-right font-data text-xs text-white">
                    <motion.span
                      animate={{ opacity: [1, 0.5, 1] }}
                      transition={{ repeat: Infinity, duration: 2 }}
                    >
                      ₹{pos.current}
                    </motion.span>
                  </td>
                  <td className={`p-6 text-right font-bold font-data text-sm ${
                    pos.pnlType === "profit" ? "text-profit glow-profit" : "text-loss glow-loss"
                  }`}>
                    {pos.pnl}
                  </td>
                  <td className="p-6 text-right">
                     <button className="text-text-secondary hover:text-purple-royal transition-colors">
                        <ExternalLink size={16} />
                     </button>
                  </td>
                </motion.tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
