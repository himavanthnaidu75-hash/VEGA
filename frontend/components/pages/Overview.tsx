"use client";
import React from "react";
import { motion } from "framer-motion";
import { ArrowUpRight, ArrowDownRight, ShieldCheck, Activity } from "lucide-react";

const stats = [
  { label: "NET REALIZED P&L", value: "+ ₹12,450.00", sub: "TODAY", type: "profit" },
  { label: "WIN RATE", value: "68.4%", sub: "NOMINAL", type: "neutral" },
  { label: "CAPITAL DEPLOYED", value: "₹45,000", sub: "3 ACTIVE", type: "neutral" },
  { label: "CURRENT DRAWDOWN", value: "-0.45%", sub: "MINIMAL", type: "loss" },
];

const watchlist = [
  { symbol: "RELIANCE", price: "2,945.60", change: "+1.2%", trend: "UP" },
  { symbol: "TCS", price: "4,120.30", change: "-0.4%", trend: "DOWN" },
  { symbol: "NIFTY 50", price: "22,456.70", change: "+0.3%", trend: "UP" },
];

export default function Overview() {
  return (
    <div className="space-y-12">
      {/* Stat Cards */}
      <div className="grid grid-cols-4 gap-6">
        {stats.map((s, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: i * 0.1 }}
            className="glass-card p-6 rounded-sm border-l-2 border-purple-royal/20"
          >
            <p className="text-[10px] text-text-secondary uppercase tracking-[0.2em] font-bold mb-2">{s.label}</p>
            <h3 className={`text-3xl font-bold font-data tracking-tighter ${
              s.type === "profit" ? "text-profit glow-profit" : s.type === "loss" ? "text-loss glow-loss" : "text-white"
            }`}>
              {s.value}
            </h3>
            <p className="text-[10px] text-text-secondary mt-2 tracking-widest">{s.sub}</p>
          </motion.div>
        ))}
      </div>

      <div className="grid grid-cols-12 gap-8">
        {/* Watchlist Matrix */}
        <div className="col-span-8 glass-card p-8 rounded-sm">
          <h3 className="text-xs text-teal-blue font-bold uppercase tracking-[0.3em] mb-8 flex items-center gap-2">
            <Activity size={16} /> Watchlist Matrix
          </h3>
          <div className="space-y-4">
            {watchlist.map((w, i) => (
              <div key={i} className="flex justify-between items-center py-4 border-b border-white/5 hover:bg-white/[0.02] transition-all px-4 rounded-sm">
                <div className="flex items-center gap-4">
                  <div className={`w-1 h-8 ${w.trend === "UP" ? "bg-profit" : "bg-loss"}`} />
                  <span className="text-lg font-bold text-white">{w.symbol}</span>
                </div>
                <div className="flex gap-12 items-center">
                  <div className="text-right">
                    <p className="text-[10px] text-text-secondary uppercase">Last Price</p>
                    <p className="font-data text-sm text-white">₹{w.price}</p>
                  </div>
                  <div className="text-right w-24">
                    <p className="text-[10px] text-text-secondary uppercase">Change</p>
                    <p className={`font-data text-sm ${w.trend === "UP" ? "text-profit" : "text-loss"}`}>
                      {w.change}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Risk Armor */}
        <div className="col-span-4 glass-card p-8 rounded-sm">
          <h3 className="text-xs text-purple-royal font-bold uppercase tracking-[0.3em] mb-8 flex items-center gap-2">
            <ShieldCheck size={16} /> Risk Armor
          </h3>
          <div className="space-y-8">
            <div>
              <div className="flex justify-between text-[10px] uppercase font-bold mb-2">
                <span className="text-text-secondary">Daily Loss Limit</span>
                <span className="text-white">₹15,000 / ₹20,000</span>
              </div>
              <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: "75%" }}
                  className="h-full bg-purple-royal shadow-[0_0_8px_#6600CC]"
                />
              </div>
            </div>
            <div>
              <div className="flex justify-between text-[10px] uppercase font-bold mb-2">
                <span className="text-text-secondary">Exposure Ratio</span>
                <span className="text-white">2.4x Leverage</span>
              </div>
              <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: "45%" }}
                  className="h-full bg-teal-blue shadow-[0_0_8px_#0096C7]"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
