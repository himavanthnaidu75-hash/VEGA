"use client";
import React from "react";
import { motion } from "framer-motion";
import { ArrowUpRight, ShieldCheck, Globe, Activity } from "lucide-react";

const mainStats = [
  { label: "REALIZED P&L", val: "+ ₹12,450.00", sub: "MARKET SESSION", type: "profit" },
  { label: "WIN PROBABILITY", val: "72.4%", sub: "NOMINAL", type: "neutral" },
  { label: "RISK EXPOSURE", val: "₹18,500", sub: "2.5x LEVERAGE", type: "neutral" },
  { label: "AVG. R MULTIPLE", val: "2.14", sub: "INSTITUTIONAL", type: "neutral" },
];

export default function Overview() {
  return (
    <div className="space-y-16">
      {/* Prime Indicators */}
      <div className="grid grid-cols-4 gap-8">
        {mainStats.map((s, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: i * 0.1, ease: "easeOut" }}
            className="glass-lux p-8 rounded-sm border-t border-gold/5"
          >
            <p className="text-[9px] text-text-secondary uppercase tracking-[0.3em] font-bold mb-4">{s.label}</p>
            <h3 className={`text-3xl font-bold font-data tracking-tighter ${
              s.type === "profit" ? "text-profit glow-profit" : "text-platinum"
            }`}>
              {s.val}
            </h3>
            <div className="mt-4 pt-4 border-t border-white/5 flex justify-between items-center">
               <span className="text-[9px] text-text-secondary uppercase tracking-widest">{s.sub}</span>
               {s.type === "profit" && <ArrowUpRight size={14} className="text-profit" />}
            </div>
          </motion.div>
        ))}
      </div>

      <div className="grid grid-cols-12 gap-12">
        {/* Watchlist Spectrum */}
        <div className="col-span-8 glass-lux p-10 rounded-sm">
           <header className="flex justify-between items-center mb-12">
              <h3 className="text-xs text-gold font-bold uppercase tracking-[0.4em] flex items-center gap-3">
                 <Activity size={16} /> Asset Spectrum
              </h3>
              <div className="flex gap-4">
                 <div className="px-4 py-1 border border-white/10 text-[9px] font-bold uppercase tracking-widest text-text-secondary">NSE:EQUITY</div>
                 <div className="px-4 py-1 border border-white/10 text-[9px] font-bold uppercase tracking-widest text-text-secondary">MCX:COMMODITIES</div>
              </div>
           </header>

           <div className="space-y-6">
              {["RELIANCE", "TCS", "HDFC BANK", "INFY", "NIFTY 50"].map((name, i) => (
                <div key={i} className="flex justify-between items-center py-5 border-b border-white/5 group hover:bg-white/[0.01] transition-all px-4">
                   <div className="flex items-center gap-6">
                      <span className="text-[10px] text-text-secondary font-data">0{i+1}</span>
                      <span className="text-lg font-bold tracking-tight text-platinum">{name}</span>
                   </div>
                   <div className="flex gap-16 items-center">
                      <div className="text-right">
                         <p className="text-[9px] text-text-secondary uppercase tracking-widest mb-1">Price</p>
                         <p className="font-data text-xs text-platinum">₹{ (2000 + (i * 450)).toLocaleString() }.00</p>
                      </div>
                      <div className="text-right w-24">
                         <p className="text-[9px] text-text-secondary uppercase tracking-widest mb-1">Change</p>
                         <p className={`font-data text-xs ${i % 2 === 0 ? "text-profit" : "text-loss"}`}>
                            {i % 2 === 0 ? "+" : "-"}{(0.2 + (i * 0.1)).toFixed(2)}%
                         </p>
                      </div>
                   </div>
                </div>
              ))}
           </div>
        </div>

        {/* System Integrity */}
        <div className="col-span-4 space-y-8">
           <div className="glass-lux p-10 rounded-sm">
              <h3 className="text-xs text-gold font-bold uppercase tracking-[0.4em] mb-10 flex items-center gap-3">
                 <ShieldCheck size={16} /> Operational Risk
              </h3>
              <div className="space-y-12">
                 <div>
                    <div className="flex justify-between text-[9px] uppercase font-bold mb-3 tracking-widest">
                       <span className="text-text-secondary">Drawdown Limit</span>
                       <span className="text-platinum">0.45% / 2.0%</span>
                    </div>
                    <div className="h-[2px] bg-white/5 relative">
                       <motion.div
                         initial={{ width: 0 }}
                         animate={{ width: "22%" }}
                         className="absolute inset-0 bg-gold shadow-[0_0_10px_#D4AF37]"
                       />
                    </div>
                 </div>
                 <div>
                    <div className="flex justify-between text-[9px] uppercase font-bold mb-3 tracking-widest">
                       <span className="text-text-secondary">Margin Allocation</span>
                       <span className="text-platinum">₹12,400 Utilized</span>
                    </div>
                    <div className="h-[2px] bg-white/5 relative">
                       <motion.div
                         initial={{ width: 0 }}
                         animate={{ width: "65%" }}
                         className="absolute inset-0 bg-platinum opacity-40 shadow-[0_0_10px_#FFFFFF]"
                       />
                    </div>
                 </div>
              </div>
           </div>

           <div className="glass-lux p-8 rounded-sm bg-gold/5 border-gold/10">
              <div className="flex items-center gap-3 mb-4">
                 <Globe size={16} className="text-gold" />
                 <h4 className="text-[10px] font-bold text-platinum uppercase tracking-[0.3em]">Institutional Node</h4>
              </div>
              <p className="text-[10px] text-text-secondary leading-loose font-light">
                Connected to NSE Gateway via <span className="text-platinum font-bold">Mumbai-Central-A</span>.
                Average execution latency stabilized at <span className="text-gold font-bold">12ms</span>.
              </p>
           </div>
        </div>
      </div>
    </div>
  );
}
