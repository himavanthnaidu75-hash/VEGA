"use client";
import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X } from "lucide-react";

const steps = [
  { id: "terminal", title: "Trade Terminal", text: "Your real-time opportunity scanner for ICT and SMC setups." },
  { id: "overview", title: "Terminal Overview", text: "Track your portfolio performance and daily risk metrics at a glance." },
  { id: "positions", title: "Positions", text: "Monitor all active trades and live unrealized P&L." },
  { id: "journal", title: "Journal", text: "Review your complete trade history and institutional performance." },
  { id: "config", title: "Engine Config", text: "Configure your trading adapter and run system diagnostics." },
];

export default function Onboarding() {
  const [show, setShow] = useState(false);
  const [step, setStep] = useState(0);

  useEffect(() => {
    const completed = localStorage.getItem("vega_onboarding_v1");
    if (!completed) setShow(true);
  }, []);

  const handleNext = () => {
    if (step < steps.length - 1) {
      setStep(step + 1);
    } else {
      complete();
    }
  };

  const complete = () => {
    localStorage.setItem("vega_onboarding_v1", "true");
    setShow(false);
  };

  if (!show) return null;

  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="fixed inset-0 z-[100] flex items-center justify-center p-8"
      >
        <div className="absolute inset-0 bg-black/90 backdrop-blur-sm" />

        <motion.div
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          className="relative glass-card max-w-md w-full p-12 rounded-sm border border-purple-royal/40 text-center"
        >
          <button
            onClick={complete}
            className="absolute top-6 right-6 text-text-secondary hover:text-white transition-colors"
          >
            <X size={20} />
          </button>

          <motion.div
            key={step}
            initial={{ x: 20, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: -20, opacity: 0 }}
            className="space-y-6"
          >
            <div className="inline-block px-3 py-1 bg-purple-royal/10 border border-purple-royal/30 text-purple-royal text-[10px] font-bold uppercase tracking-widest mb-4">
              Step {step + 1} of {steps.length}
            </div>
            <h2 className="text-3xl font-bold tracking-tighter text-white">{steps[step].title}</h2>
            <p className="text-sm text-text-secondary leading-relaxed">{steps[step].text}</p>

            <div className="pt-8">
              <button
                onClick={handleNext}
                className="w-full py-4 bg-purple-royal text-white text-xs font-bold uppercase tracking-[0.2em] hover:bg-purple-royal/80 transition-all shadow-[0_0_20px_rgba(102,0,204,0.3)]"
              >
                {step === steps.length - 1 ? "Initialize VEGA PRO" : "Next Segment"}
              </button>
              <button
                onClick={complete}
                className="mt-4 text-[10px] text-text-secondary uppercase tracking-widest hover:text-white transition-colors"
              >
                Skip Induction
              </button>
            </div>
          </motion.div>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
}
