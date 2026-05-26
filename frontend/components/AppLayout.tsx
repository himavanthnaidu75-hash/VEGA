"use client";
import React, { useState, useEffect } from "react";
import TopBar from "./TopBar";
import Onboarding from "./Onboarding";
import { motion, AnimatePresence } from "framer-motion";
import { usePathname } from "next/navigation";
import Link from "next/link";

const navItems = [
  { name: "Terminal", path: "/" },
  { name: "Portfolio", path: "/overview" },
  { name: "Vault", path: "/positions" },
  { name: "Ledger", path: "/journal" },
  { name: "System", path: "/logs" },
  { name: "Control", path: "/config" },
];

export default function AppLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return <div className="min-h-screen bg-bg-pure" />;
  }

  return (
    <div className="min-h-screen relative text-platinum">
      <TopBar />
      <Onboarding />

      {/* Navigation Layer */}
      <div className="fixed top-14 left-0 right-0 h-10 bg-black/20 border-b border-border-lux/30 z-40 flex items-center justify-center gap-10 backdrop-blur-md">
        {navItems.map((item) => (
          <Link key={item.path} href={item.path}>
            <span className={`text-[9px] uppercase tracking-[0.4em] font-bold cursor-pointer transition-all hover:text-gold ${
              pathname === item.path ? "text-gold border-b border-gold" : "text-text-secondary"
            }`}>
              {item.name}
            </span>
          </Link>
        ))}
      </div>

      <main className="pt-32 pb-16 px-12">
        <AnimatePresence mode="wait">
          <motion.div
            key={pathname}
            initial={{ opacity: 0, filter: "blur(10px)", scale: 0.98 }}
            animate={{ opacity: 1, filter: "blur(0px)", scale: 1 }}
            exit={{ opacity: 0, filter: "blur(10px)", scale: 0.98 }}
            transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
          >
            {children}
          </motion.div>
        </AnimatePresence>
      </main>
    </div>
  );
}
