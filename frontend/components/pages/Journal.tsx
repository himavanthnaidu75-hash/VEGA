"use client";
import React from "react";
import { motion } from "framer-motion";
import { BookOpen, TrendingUp, TrendingDown } from "lucide-react";

const journalEntries = [
  { id: "TXN-882", date: "2024-05-26", symbol: "RELIANCE.NS", side: "BUY", result: "WIN", pnl: "+₹3,450.00", rr: "1:2.4" },
  { id: "TXN-881", date: "2024-05-26", symbol: "INFY.NS", side: "SELL", result: "LOSS", pnl: "-₹1,200.00", rr: "1:1.5" },
  { id: "TXN-880", date: "2024-05-25", symbol: "TCS.NS", side: "BUY", result: "WIN", pnl: "+₹5,120.00", rr: "1:3.1" },
  { id: "TXN-879", date: "2024-05-25", symbol: "HDFC.NS", side: "SELL", result: "WIN", pnl: "+₹2,200.00", rr: "1:2.0" },
];

export default function Journal() {
  return (
    <div className="space-y-8">
      <header className="flex justify-between items-end">
        <div className="flex flex-col">
          <h2 className="text-4xl font-light tracking-tighter text-white uppercase">Journal</h2>
          <span className="text-[10px] text-teal-blue tracking-[0.3em] font-bold uppercase mt-1">
            Historical Performance Ledger
          </span>
        </div>
        <div className="flex gap-12 bg-white/[0.02] border border-white/5 p-6 rounded-sm">
           <div className="text-right">
              <p className="text-[8px] text-text-secondary uppercase mb-1">Total Trades</p>
              <p className="font-data text-xl font-bold">124</p>
           </div>
           <div className="text-right">
              <p className="text-[8px] text-text-secondary uppercase mb-1">Win Rate</p>
              <p className="font-data text-xl font-bold text-profit">68.4%</p>
           </div>
           <div className="text-right">
              <p className="text-[8px] text-text-secondary uppercase mb-1">Total P&L</p>
              <p className="font-data text-xl font-bold text-profit glow-profit">+₹48,250.00</p>
           </div>
        </div>
      </header>

      <div className="glass-card rounded-sm overflow-hidden">
        <table className="w-full text-left">
          <thead>
            <tr className="border-b border-white/5 bg-white/[0.02]">
              <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold">Ref ID</th>
              <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold">Date</th>
              <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold">Instrument</th>
              <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold text-center">Result</th>
              <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold text-right">R:R</th>
              <th className="p-6 text-[10px] text-text-secondary uppercase tracking-widest font-bold text-right">Realized P&L</th>
            </tr>
          </thead>
          <tbody>
            {journalEntries.map((entry, i) => (
              <motion.tr
                key={i}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.05 }}
                className="border-b border-white/5 hover:bg-white/[0.02] transition-all group relative"
              >
                {/* Win/Loss Indicator Border */}
                <td className={`absolute left-0 top-0 bottom-0 w-[2px] ${
                  entry.result === "WIN" ? "bg-profit" : "bg-loss"
                }`} />

                <td className="p-6 text-xs font-data text-text-secondary">{entry.id}</td>
                <td className="p-6 text-xs text-white">{entry.date}</td>
                <td className="p-6">
                  <div className="flex flex-col">
                    <span className="text-sm font-bold text-white">{entry.symbol}</span>
                    <span className="text-[10px] text-text-secondary uppercase tracking-widest font-bold">{entry.side}</span>
                  </div>
                </td>
                <td className="p-6 text-center">
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                    entry.result === "WIN" ? "bg-profit/10 text-profit" : "bg-loss/10 text-loss"
                  }`}>
                    {entry.result}
                  </span>
                </td>
                <td className="p-6 text-right font-data text-xs text-white">{entry.rr}</td>
                <td className={`p-6 text-right font-bold font-data text-sm ${
                  entry.result === "WIN" ? "text-profit" : "text-loss"
                }`}>
                  {entry.pnl}
                </td>
              </motion.tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
