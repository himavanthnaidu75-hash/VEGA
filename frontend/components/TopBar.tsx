"use client";
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Wifi, Clock, Anchor } from "lucide-react";

const stocks = [
  { s: "NIFTY 50", p: "22,456.70", c: "+0.3%" },
  { s: "BANK NIFTY", p: "47,890.00", c: "-0.1%" },
  { s: "RELIANCE", p: "2,945.60", c: "+1.2%" },
  { s: "TCS", p: "4,120.30", c: "-0.4%" },
  { s: "HDFC BANK", p: "1,450.90", c: "+0.2%" },
];

export default function TopBar() {
  const [time, setTime] = useState("");
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString([], { hour12: false }));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  if (!mounted) {
    return <div className="fixed top-0 left-0 right-0 h-14 border-b border-border-lux bg-black/40 backdrop-blur-2xl z-50" />;
  }

  return (
    <div className="fixed top-0 left-0 right-0 h-14 border-b border-border-lux bg-black/40 backdrop-blur-2xl z-50 flex items-center px-10">
      {/* Wordmark */}
      <div className="flex-shrink-0 flex items-center gap-3">
        <h1 className="text-lg font-bold tracking-[0.3em] text-platinum">
          VEGA <span className="text-gold">PRO</span>
        </h1>
        <div className="h-4 w-[1px] bg-border-lux" />
        <span className="text-[8px] text-text-secondary uppercase tracking-[0.5em] font-bold">Swiss Engine v3.0</span>
      </div>

      {/* Ticker */}
      <div className="flex-1 overflow-hidden mx-16">
        <div className="flex animate-marquee whitespace-nowrap gap-16">
          {[...stocks, ...stocks].map((s, i) => (
            <div key={i} className="flex items-center gap-3 font-data text-[10px]">
              <span className="text-text-secondary">{s.s}</span>
              <span className="text-platinum font-bold">{s.p}</span>
              <span className={s.c.startsWith("+") ? "text-profit" : "text-loss"}>{s.c}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Status Indicators */}
      <div className="flex items-center gap-8">
        <div className="flex items-center gap-2">
          <div className="w-1.5 h-1.5 rounded-full bg-gold animate-pulse shadow-[0_0_10px_#D4AF37]" />
          <span className="text-[9px] font-bold text-gold uppercase tracking-widest">Live Terminal</span>
        </div>
        <div className="flex items-center gap-2 text-text-secondary">
          <Wifi size={12} className="text-gold opacity-50" />
          <span className="font-data text-[10px] tracking-tighter">98MS</span>
        </div>
        <div className="flex items-center gap-3 text-text-secondary border-l border-border-lux pl-6">
          <Clock size={12} className="text-gold opacity-50" />
          <span className="font-data text-[10px] tracking-tighter">{time}</span>
        </div>
      </div>

      <style jsx>{`
        @keyframes marquee {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
        }
        .animate-marquee {
          animation: marquee 40s linear infinite;
        }
      `}</style>
    </div>
  );
}
