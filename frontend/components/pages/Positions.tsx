"use client";
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { ShieldCheck, ArrowRight, Target, Lock } from "lucide-react";

const positions = [
  { symbol: "RELIANCE.NS", side: "BUY", qty: 50, entry: "2,940.00", curr: "2,945.60", pnl: "+ ₹280.00", pnlType: "profit" },
  { symbol: "TCS.NS", side: "SELL", qty: 25, entry: "4,125.00", curr: "4,120.30", pnl: "+ ₹117.50", pnlType: "profit" },
];

export default function Positions() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => setLoading(false), 1200);
  }, []);

  return (
    <div className="space-y-12">
      <header className="flex flex-col">
        <h2 className="text-4xl font-bold tracking-tighter text-platinum">VAULT</h2>
        <p className="text-[10px] text-gold tracking-[0.4em] font-bold uppercase mt-1">Live Asset Exposure Control</p>
      </header>

      {loading ? (
        <div className="grid grid-cols-1 gap-6">
           {[1, 2].map(i => (
             <div key={i} className="h-32 w-full glass-lux animate-pulse rounded-sm" />
           ))}
        </div>
      ) : (
        <div className="glass-lux rounded-sm overflow-hidden border border-border-lux/20">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-white/5 bg-white/[0.01]">
                <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.3em] font-bold">Instrument</th>
                <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.3em] font-bold">Execution</th>
                <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.3em] font-bold text-right">Entry</th>
                <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.3em] font-bold text-right">Market</th>
                <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.3em] font-bold text-right">Position P&L</th>
                <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.3em] font-bold text-right">Control</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/5">
              {positions.map((pos, i) => (
                <motion.tr
                  key={i}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: i * 0.1 }}
                  className="hover:bg-white/[0.01] transition-all group"
                >
                  <td className="p-8">
                    <div className="flex items-center gap-4">
                       <div className="w-1.5 h-1.5 rounded-full bg-gold" />
                       <div className="flex flex-col">
                          <span className="text-sm font-bold text-platinum tracking-tight">{pos.symbol}</span>
                          <span className="text-[9px] text-text-secondary uppercase tracking-widest font-bold">Equity // NSE</span>
                       </div>
                    </div>
                  </td>
                  <td className="p-8">
                    <div className="flex flex-col gap-1">
                       <span className={`text-[9px] font-bold px-2 py-0.5 rounded-sm inline-block w-fit border ${
                         pos.side === "BUY" ? "border-profit/20 text-profit bg-profit/5" : "border-loss/20 text-loss bg-loss/5"
                       }`}>
                         {pos.side}
                       </span>
                       <span className="text-[9px] text-text-secondary font-data">QTY: {pos.qty}</span>
                    </div>
                  </td>
                  <td className="p-8 text-right font-data text-xs text-platinum">₹{pos.entry}</td>
                  <td className="p-8 text-right font-data text-xs text-platinum">
                    <motion.span animate={{ opacity: [1, 0.5, 1] }} transition={{ repeat: Infinity, duration: 2 }}>
                       ₹{pos.curr}
                    </motion.span>
                  </td>
                  <td className={`p-8 text-right font-bold font-data text-sm ${
                    pos.pnlType === "profit" ? "text-profit glow-profit" : "text-loss glow-loss"
                  }`}>
                    {pos.pnl}
                  </td>
                  <td className="p-8 text-right">
                     <button className="text-text-secondary hover:text-gold transition-colors flex items-center justify-end gap-2 text-[9px] uppercase font-bold tracking-widest">
                        Manage <ArrowRight size={12} />
                     </button>
                  </td>
                </motion.tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Vault Footer */}
      <div className="flex justify-between items-center py-6 border-t border-white/5">
         <div className="flex gap-8">
            <div className="flex items-center gap-2">
               <Target size={14} className="text-gold" />
               <span className="text-[9px] text-text-secondary uppercase font-bold tracking-widest">Stop Loss Engine: <span className="text-platinum">NOMINAL</span></span>
            </div>
            <div className="flex items-center gap-2">
               <Lock size={14} className="text-gold" />
               <span className="text-[9px] text-text-secondary uppercase font-bold tracking-widest">Execution Lock: <span className="text-platinum">ENABLED</span></span>
            </div>
         </div>
         <p className="text-[9px] text-text-secondary italic">Vault secured with 256-bit institutional encryption.</p>
      </div>
    </div>
  );
}
