"use client";
import React, { useState } from "react";
import { motion } from "framer-motion";
import { Shield, Play, Sliders, CheckCircle, Radio } from "lucide-react";

export default function Config() {
  const [activeMode, setActiveMode] = useState("SIM");

  return (
    <div className="space-y-12">
      <header className="flex flex-col">
        <h2 className="text-4xl font-bold tracking-tighter text-platinum">CONTROL</h2>
        <p className="text-[10px] text-gold tracking-[0.4em] font-bold uppercase mt-1">Platform Logic & Environment</p>
      </header>

      <div className="grid grid-cols-2 gap-12">
        {/* Environment Matrix */}
        <div className="space-y-10">
          <h3 className="text-xs text-text-secondary font-bold uppercase tracking-[0.4em] flex items-center gap-3">
             <Radio size={16} className="text-gold" /> Environment Matrix
          </h3>
          <div className="grid grid-cols-2 gap-8">
             <div
               onClick={() => setActiveMode("SIM")}
               className={`glass-lux p-8 rounded-sm cursor-pointer transition-all duration-500 border-l-4 ${
                 activeMode === "SIM" ? "border-gold bg-gold/5 shadow-[0_0_30px_rgba(212,175,55,0.1)]" : "border-white/5 opacity-40 grayscale"
               }`}
             >
                <div className="flex items-center gap-3 mb-6">
                   <div className={`w-2 h-2 rounded-full ${activeMode === "SIM" ? "bg-gold animate-pulse" : "bg-text-secondary"}`} />
                   <span className="text-[10px] font-bold text-platinum uppercase tracking-widest">Simulation Mode</span>
                </div>
                <p className="text-[10px] text-text-secondary leading-loose font-light">
                  Executing via Paper-Trading adapter. Real-time market data with simulated risk exposure.
                </p>
             </div>
             <div
               onClick={() => setActiveMode("LIVE")}
               className={`glass-lux p-8 rounded-sm cursor-pointer transition-all duration-500 border-l-4 ${
                 activeMode === "LIVE" ? "border-loss bg-loss/5 shadow-[0_0_30px_rgba(255,59,59,0.1)]" : "border-white/5 opacity-40 grayscale"
               }`}
             >
                <div className="flex items-center gap-3 mb-6">
                   <div className={`w-2 h-2 rounded-full ${activeMode === "LIVE" ? "bg-loss animate-pulse" : "bg-text-secondary"}`} />
                   <span className="text-[10px] font-bold text-platinum uppercase tracking-widest">Live Execution</span>
                </div>
                <p className="text-[10px] text-text-secondary leading-loose font-light">
                  Direct market access via Dhan API. Real capital exposure. Institutional safeguards active.
                </p>
             </div>
          </div>
        </div>

        {/* Strategy Matrix */}
        <div className="space-y-10">
           <h3 className="text-xs text-text-secondary font-bold uppercase tracking-[0.4em] flex items-center gap-3">
             <Sliders size={16} className="text-gold" /> Strategy Matrix
          </h3>
          <div className="glass-lux p-10 rounded-sm space-y-8">
             {[
               { name: "Institutional Liquidity Sweep", desc: "Detection of major stop-runs" },
               { name: "Fair Value Gap (FVG)", desc: "Imbalance identification" },
               { name: "BOS / CHoCH Alignment", desc: "Market structure shift confirmation" },
               { name: "Volume Profile POC", desc: "Institutional anchor mapping" },
             ].map((s, i) => (
               <div key={i} className="flex justify-between items-center group">
                 <div className="flex flex-col">
                    <span className="text-xs font-bold text-platinum tracking-tight group-hover:text-gold transition-colors">{s.name}</span>
                    <span className="text-[9px] text-text-secondary uppercase tracking-widest mt-1">{s.desc}</span>
                 </div>
                 <div className="w-12 h-5 rounded-full bg-white/5 border border-white/10 relative p-1 cursor-pointer">
                    <motion.div
                      layout
                      initial={false}
                      className="w-3 h-3 bg-gold rounded-full"
                    />
                 </div>
               </div>
             ))}
          </div>
        </div>
      </div>
    </div>
  );
}
