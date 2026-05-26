"use client";
import React, { useState, useEffect, useRef } from "react";
import { Cpu, Terminal as TerminalIcon } from "lucide-react";

const logs = [
  "SYSTEM_INITIALIZE [NOMINAL]",
  "DHAN_GATEWAY_LINKED (ID: DX-442)",
  "ICT_SCANNER_HANDSHAKE_COMPLETE",
  "AURORA_ENGINE_READY",
  "RELIANCE.NS: FVG_DELIVERY_DETECTED",
  "TCS.NS: LIQUIDITY_SWEEP_CONFIRMED",
  "EXECUTING_ALGO_ORDER [SIDE:SELL]",
  "ORDER_FILLED: 4125.00 [LATENCY: 12MS]",
  "MONITORING_ORB_BREAKOUT...",
];

export default function Logs() {
  const [activeLogs, setActiveLogs] = useState<string[]>([]);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      if (i < logs.length) {
        setActiveLogs(prev => [...prev, `[${new Date().toLocaleTimeString([], { hour12: false })}] VEGA_KERNEL: ${logs[i]}`]);
        i++;
      } else {
        clearInterval(interval);
      }
    }, 1200);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
  }, [activeLogs]);

  return (
    <div className="space-y-12">
      <header className="flex justify-between items-end">
        <div className="space-y-1">
          <h2 className="text-4xl font-bold tracking-tighter text-platinum">SYSTEM</h2>
          <p className="text-[10px] text-gold tracking-[0.4em] font-bold uppercase">Kernel Runtime Data</p>
        </div>
        <div className="flex gap-6 items-center bg-white/[0.02] border border-white/5 px-8 py-4 rounded-sm">
           <Cpu size={14} className="text-gold" />
           <span className="text-[10px] font-bold text-text-secondary uppercase tracking-[0.3em]">Core Integrity: 100%</span>
        </div>
      </header>

      <div className="relative glass-lux bg-black/60 h-[600px] p-10 rounded-sm overflow-hidden border border-border-lux/10">
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-gold/[0.02] to-transparent pointer-events-none" />

        <div
          ref={scrollRef}
          className="h-full overflow-y-auto custom-scrollbar space-y-4 relative z-10"
        >
          {activeLogs.map((log, i) => (
            <div key={i} className="flex gap-6 items-start font-data text-[11px] group">
               <span className="text-gold opacity-30 group-hover:opacity-100 transition-opacity">#</span>
               <span className="text-platinum/80 leading-relaxed tracking-tight group-hover:text-platinum transition-colors">{log}</span>
            </div>
          ))}
          <div className="flex gap-6 items-center">
            <span className="text-gold opacity-30 animate-pulse">#</span>
            <div className="w-2 h-4 bg-gold/60 animate-pulse" />
          </div>
        </div>
      </div>
    </div>
  );
}
