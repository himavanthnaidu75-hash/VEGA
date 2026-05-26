"use client";
import React, { useState, useEffect, useRef } from "react";
import { Terminal as TerminalIcon } from "lucide-react";

const mockLogs = [
  "INITIALIZING VEGA CORE...",
  "AUTHENTICATING DHAN API LINK...",
  "CONNECTED: 98ms LATENCY",
  "LOADING ICT SCANNER MODULE...",
  "SCANNING NIFTY 50 WATCHLIST...",
  "RELIANCE.NS - PDH LIQUIDITY SWEEP DETECTED",
  "RELIANCE.NS - 15M FVG CONFIRMED",
  "TCS.NS - BEARISH ORDER BLOCK MITIGATED",
  "EXECUTING SELL ORDER: TCS.NS (25 QTY)",
  "ORDER FILLED @ 4125.00",
  "UPDATING TRAILING STOP LOSS: 4138.00",
];

export default function Logs() {
  const [logs, setLogs] = useState<string[]>([]);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      if (i < mockLogs.length) {
        setLogs(prev => [...prev, `[${new Date().toLocaleTimeString()}] ${mockLogs[i]}`]);
        i++;
      } else {
        clearInterval(interval);
      }
    }, 1500);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs]);

  return (
    <div className="space-y-8 h-full">
      <header className="flex flex-col">
        <h2 className="text-4xl font-light tracking-tighter text-white uppercase">System Logs</h2>
        <span className="text-[10px] text-teal-blue tracking-[0.3em] font-bold uppercase mt-1">
          Raw Kernel Output
        </span>
      </header>

      <div className="relative glass-card rounded-sm bg-black h-[600px] p-8 overflow-hidden font-data text-xs border border-purple-royal/20">
        <div className="absolute inset-0 crt-overlay opacity-20 pointer-events-none" />
        <div className="absolute inset-0 scanline pointer-events-none" />

        <div
          ref={scrollRef}
          className="h-full overflow-y-auto custom-scrollbar space-y-2 relative z-10"
        >
          {logs.map((log, i) => (
            <div key={i} className="flex gap-4">
               <span className="text-teal-blue opacity-50 shrink-0">{">"}</span>
               <span className="text-teal-blue/80 leading-relaxed">{log}</span>
            </div>
          ))}
          <div className="flex gap-4 items-center">
            <span className="text-teal-blue opacity-50 shrink-0">{">"}</span>
            <div className="w-2 h-4 bg-teal-blue/80 animate-pulse" />
          </div>
        </div>
      </div>
    </div>
  );
}
