"use client";
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Book, ChevronRight, FileText } from "lucide-react";

const history = [
  { ref: "TX-0124", date: "2024.05.26", sym: "RELIANCE.NS", side: "BUY", res: "WIN", pnl: "+ ₹3,450.00", rr: "1:2.4" },
  { ref: "TX-0123", date: "2024.05.26", sym: "INFY.NS", side: "SELL", res: "LOSS", pnl: "- ₹1,200.00", rr: "1:1.5" },
  { ref: "TX-0122", date: "2024.05.25", sym: "TCS.NS", side: "BUY", res: "WIN", pnl: "+ ₹5,120.00", rr: "1:3.1" },
];

export default function Journal() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return <div className="min-h-screen bg-bg-pure" />;
  }

  return (
    <div className="space-y-12">
      <header className="flex justify-between items-end">
        <div className="space-y-1">
          <h2 className="text-4xl font-bold tracking-tighter text-platinum">LEDGER</h2>
          <p className="text-[10px] text-gold tracking-[0.4em] font-bold uppercase">Institutional Audit History</p>
        </div>
        <div className="glass-lux px-10 py-6 rounded-sm flex gap-12 border-l-2 border-gold/40">
           <div className="text-right">
              <p className="text-[8px] text-text-secondary uppercase tracking-[0.2em] mb-2 font-bold">Success Rate</p>
              <p className="font-data text-xl font-bold text-profit">72.4%</p>
           </div>
           <div className="h-8 w-[1px] bg-white/5 my-auto" />
           <div className="text-right">
              <p className="text-[8px] text-text-secondary uppercase tracking-[0.2em] mb-2 font-bold">Total Gain</p>
              <p className="font-data text-xl font-bold text-profit glow-profit">+₹48,250</p>
           </div>
        </div>
      </header>

      <div className="glass-lux rounded-sm border border-border-lux/10 overflow-hidden">
        <table className="w-full text-left">
          <thead>
            <tr className="border-b border-white/5 bg-white/[0.01]">
              <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.4em] font-bold">Reference</th>
              <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.4em] font-bold">Timestamp</th>
              <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.4em] font-bold">Instrument</th>
              <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.4em] font-bold text-center">Outcome</th>
              <th className="p-8 text-[9px] text-text-secondary uppercase tracking-[0.4em] font-bold text-right">Yield</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {history.map((h, i) => (
              <motion.tr
                key={i}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.05 }}
                className="hover:bg-white/[0.01] transition-all group cursor-pointer"
              >
                <td className="p-8 font-data text-[11px] text-text-secondary">{h.ref}</td>
                <td className="p-8 font-data text-[11px] text-platinum opacity-60">{h.date}</td>
                <td className="p-8">
                   <div className="flex flex-col">
                      <span className="text-sm font-bold text-platinum tracking-tight">{h.sym}</span>
                      <span className="text-[9px] text-text-secondary font-bold uppercase tracking-widest">{h.side} // {h.rr}</span>
                   </div>
                </td>
                <td className="p-8 text-center">
                   <span className={`text-[9px] font-bold px-3 py-0.5 rounded-sm ${
                     h.res === "WIN" ? "text-profit bg-profit/10 border border-profit/20" : "text-loss bg-loss/10 border border-loss/20"
                   }`}>
                     {h.res}
                   </span>
                </td>
                <td className={`p-8 text-right font-bold font-data text-sm ${
                  h.res === "WIN" ? "text-profit" : "text-loss"
                }`}>
                  {h.pnl}
                </td>
              </motion.tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
