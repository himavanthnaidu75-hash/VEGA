"use client";
import React from "react";
import { motion } from "framer-motion";
import { Wifi, Clock, ShieldCheck } from "lucide-react";

const stocks = [
  { symbol: "RELIANCE", price: "2,945.60", change: "+1.2%" },
  { symbol: "TCS", price: "4,120.30", change: "-0.4%" },
  { symbol: "INFY", price: "1,680.15", change: "+0.8%" },
  { symbol: "HDFC BANK", price: "1,450.90", change: "-1.1%" },
  { symbol: "NIFTY 50", price: "22,456.70", change: "+0.3%" },
];

export default function TopBar() {
  return (
    <div className="fixed top-0 left-0 right-0 h-16 border-b border-border-subtle bg-black/80 backdrop-blur-md z-50 flex items-center px-8">
      {/* Logo */}
      <div className="flex-shrink-0">
        <h1 className="text-xl font-bold tracking-[0.2em] text-white flex items-center gap-2">
          VEGA <span className="text-purple-royal">PRO</span>
        </h1>
        <div className="h-[2px] w-full bg-gradient-to-r from-transparent via-purple-royal/50 to-transparent blur-[2px]" />
      </div>

      {/* Ticker */}
      <div className="flex-1 overflow-hidden mx-12">
        <div className="flex animate-marquee whitespace-nowrap gap-12">
          {[...stocks, ...stocks].map((s, i) => (
            <div key={i} className="flex items-center gap-2 font-data text-xs">
              <span className="text-text-secondary">{s.symbol}</span>
              <span className="text-white font-bold">{s.price}</span>
              <span className={s.change.startsWith("+") ? "text-profit" : "text-loss"}>
                {s.change}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Right Section */}
      <div className="flex items-center gap-6">
        <div className="flex items-center gap-2 text-[10px] text-teal-blue uppercase tracking-widest font-bold">
          <Wifi size={12} />
          <span>98ms Link</span>
        </div>
        <div className="flex items-center gap-2 text-[10px] text-text-secondary uppercase tracking-widest font-bold">
          <ShieldCheck size={12} />
          <span className="bg-purple-royal/20 text-purple-royal px-2 py-0.5 rounded border border-purple-royal/30">Nominal</span>
        </div>
        <div className="flex items-center gap-2 text-xs font-data text-text-secondary">
          <Clock size={12} />
          <span>{new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })}</span>
        </div>
        <div className="flex items-center gap-2">
           <div className="w-2 h-2 rounded-full bg-purple-royal animate-pulse shadow-[0_0_8px_#6600CC]" />
           <span className="text-[10px] font-bold tracking-tighter text-purple-royal uppercase">Live</span>
        </div>
      </div>

      <style jsx>{`
        @keyframes marquee {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
        }
        .animate-marquee {
          animation: marquee 30s linear infinite;
        }
      `}</style>
    </div>
  );
}
