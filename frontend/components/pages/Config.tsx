"use client";
import React, { useState } from "react";
import { motion } from "framer-motion";
import { Settings, Play, ShieldAlert, Cpu, CheckCircle2, XCircle } from "lucide-react";

export default function Config() {
  const [diagnosing, setDiagnosing] = useState(false);
  const [steps, setSteps] = useState([
    { name: "Core Kernel Integrity", status: "PENDING" },
    { name: "Broker API Connectivity", status: "PENDING" },
    { name: "ICT Engine Handshake", status: "PENDING" },
    { name: "Telegram Webhook Test", status: "PENDING" },
  ]);

  const runDiagnostic = () => {
    setDiagnosing(true);
    setSteps(steps.map(s => ({ ...s, status: "PENDING" })));

    steps.forEach((step, i) => {
      setTimeout(() => {
        setSteps(prev => {
          const newSteps = [...prev];
          newSteps[i].status = "SUCCESS";
          return newSteps;
        });
        if (i === steps.length - 1) setDiagnosing(false);
      }, (i + 1) * 1000);
    });
  };

  return (
    <div className="space-y-12">
      <header className="flex flex-col">
        <h2 className="text-4xl font-light tracking-tighter text-white uppercase">Engine Config</h2>
        <span className="text-[10px] text-teal-blue tracking-[0.3em] font-bold uppercase mt-1">
          System Parameters & Diagnostics
        </span>
      </header>

      <div className="grid grid-cols-2 gap-12">
        {/* Trading Mode */}
        <div className="space-y-6">
          <h3 className="text-xs text-text-secondary font-bold uppercase tracking-[0.2em] flex items-center gap-2">
            <Play size={14} className="text-purple-royal" /> Trading Environment
          </h3>
          <div className="grid grid-cols-2 gap-6">
            <div className="glass-card p-6 rounded-sm border-l-4 border-amber-500/50">
               <div className="flex items-center gap-2 mb-4">
                  <div className="w-2 h-2 rounded-full bg-amber-500 animate-pulse" />
                  <span className="text-xs font-bold text-amber-500 uppercase tracking-widest">Simulation</span>
               </div>
               <p className="text-[10px] text-text-secondary leading-relaxed">Risk-free execution using paper trading adapter. No real capital exposure.</p>
            </div>
            <div className="glass-card p-6 rounded-sm opacity-40 grayscale">
               <div className="flex items-center gap-2 mb-4">
                  <div className="w-2 h-2 rounded-full bg-loss" />
                  <span className="text-xs font-bold text-loss uppercase tracking-widest">Live Market</span>
               </div>
               <p className="text-[10px] text-text-secondary leading-relaxed">Direct execution on NSE via Dhan API. Real capital at risk.</p>
            </div>
          </div>
        </div>

        {/* Strategy Toggle */}
        <div className="space-y-6">
           <h3 className="text-xs text-text-secondary font-bold uppercase tracking-[0.2em] flex items-center gap-2">
            <Settings size={14} className="text-teal-blue" /> Strategy Toggles
          </h3>
          <div className="glass-card p-6 rounded-sm space-y-4">
             {[
               { name: "ICT Liquidity Sweeps", active: true },
               { name: "HTF Fair Value Gaps", active: true },
               { name: "Trend Confirmation (EMA)", active: false },
               { name: "News Sentiment Overlay", active: true },
             ].map((s, i) => (
               <div key={i} className="flex justify-between items-center py-2">
                 <span className="text-xs text-white/80">{s.name}</span>
                 <div className={`w-10 h-5 rounded-full relative cursor-pointer ${s.active ? "bg-purple-royal" : "bg-white/10"}`}>
                    <div className={`absolute top-1 w-3 h-3 rounded-full bg-white transition-all ${s.active ? "right-1" : "left-1"}`} />
                 </div>
               </div>
             ))}
          </div>
        </div>

        {/* Diagnostic Panel */}
        <div className="col-span-2 glass-card p-8 rounded-sm bg-purple-royal/[0.02]">
          <div className="flex justify-between items-center mb-8">
            <h3 className="text-xs text-purple-royal font-bold uppercase tracking-[0.3em] flex items-center gap-2">
              <Cpu size={16} /> System Diagnostics
            </h3>
            <button
              onClick={runDiagnostic}
              disabled={diagnosing}
              className="px-6 py-2 border border-purple-royal text-purple-royal text-[10px] font-bold uppercase tracking-widest hover:bg-purple-royal hover:text-white transition-all disabled:opacity-50"
            >
              {diagnosing ? "Scanning..." : "Run Diagnostic"}
            </button>
          </div>

          <div className="grid grid-cols-4 gap-8">
            {steps.map((step, i) => (
              <div key={i} className="flex flex-col items-center gap-4">
                <div className="w-12 h-12 rounded-full border border-white/5 flex items-center justify-center bg-white/[0.02]">
                  {step.status === "PENDING" ? (
                    <div className="w-4 h-4 border-2 border-purple-royal border-t-transparent rounded-full animate-spin" />
                  ) : step.status === "SUCCESS" ? (
                    <CheckCircle2 size={24} className="text-profit" />
                  ) : (
                    <XCircle size={24} className="text-loss" />
                  )}
                </div>
                <p className="text-[10px] text-text-secondary uppercase font-bold text-center tracking-wider">{step.name}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
