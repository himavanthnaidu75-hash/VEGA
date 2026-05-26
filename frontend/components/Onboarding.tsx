"use client";
import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, ChevronRight } from "lucide-react";

const steps = [
  { id: "terminal", title: "PRECISION SCANNER", text: "Autonomous identification of high-probability ICT and SMC opportunities." },
  { id: "portfolio", title: "STRATEGIC OVERVIEW", text: "Comprehensive multi-asset performance metrics and real-time capital tracking." },
  { id: "vault", title: "ACTIVE EXPOSURE", text: "Encrypted management of live market positions and risk parameters." },
  { id: "ledger", title: "AUDIT TRAIL", text: "A detailed historical record of every decision, entry, and institutional outcome." },
  { id: "system", title: "KERNEL DIAGNOSTICS", text: "Low-level system logs and autonomous configuration control." },
];

export default function Onboarding() {
  const [show, setShow] = useState(false);
  const [step, setStep] = useState(-1); // -1 for initial logo reveal

  useEffect(() => {
    const completed = localStorage.getItem("vega_onboarding_v3");
    if (!completed) setShow(true);
  }, []);

  const complete = () => {
    localStorage.setItem("vega_onboarding_v3", "true");
    setShow(false);
  };

  if (!show) return null;

  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="fixed inset-0 z-[100] flex items-center justify-center p-8 bg-black/95 backdrop-blur-xl"
      >
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(212,175,55,0.05),transparent_70%)]" />

        <div className="relative max-w-lg w-full text-center">
          {step === -1 ? (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="space-y-8"
            >
              <h1 className="text-5xl font-bold tracking-[0.4em] text-platinum">
                VEGA <span className="text-gold">PRO</span>
              </h1>
              <p className="text-[10px] text-text-secondary uppercase tracking-[0.5em] leading-loose">
                Initializing Swiss Engineering Core<br/>Institutional Grade Autonomous Trading
              </p>
              <motion.button
                whileHover={{ scale: 1.05, letterSpacing: "0.6em" }}
                onClick={() => setStep(0)}
                className="mt-12 px-10 py-4 border border-gold/40 text-gold text-[10px] font-bold uppercase tracking-[0.4em] transition-all"
              >
                Enter Terminal
              </motion.button>
            </motion.div>
          ) : (
            <motion.div
              key={step}
              initial={{ x: 20, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              exit={{ x: -20, opacity: 0 }}
              className="space-y-8"
            >
              <div className="inline-block px-4 py-1 border border-gold/20 bg-gold/5 text-gold text-[9px] font-bold uppercase tracking-[0.3em]">
                Segment {step + 1} // {steps.length}
              </div>
              <h2 className="text-3xl font-bold tracking-tight text-platinum">{steps[step].title}</h2>
              <p className="text-sm text-text-secondary leading-relaxed font-light">{steps[step].text}</p>

              <div className="pt-12 flex flex-col items-center gap-4">
                <button
                  onClick={() => step === steps.length - 1 ? complete() : setStep(step + 1)}
                  className="w-full py-4 bg-gold text-black text-[10px] font-bold uppercase tracking-[0.3em] hover:bg-white transition-all flex items-center justify-center gap-2"
                >
                  {step === steps.length - 1 ? "Initialize Core" : "Proceed"} <ChevronRight size={14} />
                </button>
                <button
                  onClick={complete}
                  className="text-[9px] text-text-secondary uppercase tracking-[0.3em] hover:text-white transition-colors"
                >
                  Skip Induction
                </button>
              </div>
            </motion.div>
          )}
        </div>

        {/* Cinematic Borders */}
        <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-gold/20 to-transparent" />
        <div className="absolute bottom-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-gold/20 to-transparent" />
      </motion.div>
    </AnimatePresence>
  );
}
