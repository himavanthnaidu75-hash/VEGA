"use client";
import React from "react";
import TopBar from "./TopBar";
import Onboarding from "./Onboarding";
import LuxCanvas from "./LuxCanvas";
import { motion, AnimatePresence } from "framer-motion";
import { usePathname } from "next/navigation";
import Link from "next/link";

const navItems = [
  { name: "Trade Terminal", path: "/" },
  { name: "Overview", path: "/overview" },
  { name: "Positions", path: "/positions" },
  { name: "Journal", path: "/journal" },
  { name: "Logs", path: "/logs" },
  { name: "Config", path: "/config" },
];

export default function AppLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  return (
    <div className="min-h-screen relative">
      <LuxCanvas />
      <Onboarding />
      <TopBar />

      {/* Sub Nav */}
      <div className="fixed top-16 left-0 right-0 h-12 bg-black/40 border-b border-border-subtle/50 z-40 flex items-center justify-center gap-8">
        {navItems.map((item) => (
          <Link key={item.path} href={item.path}>
            <span className={`text-[10px] uppercase tracking-[0.2em] font-bold cursor-pointer transition-all hover:text-purple-royal ${
              pathname === item.path ? "text-purple-royal border-b border-purple-royal" : "text-text-secondary"
            }`}>
              {item.name}
            </span>
          </Link>
        ))}
      </div>

      <main className="pt-32 pb-12 px-8">
        <AnimatePresence mode="wait">
          <motion.div
            key={pathname}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.3 }}
          >
            {children}
          </motion.div>
        </AnimatePresence>
      </main>
    </div>
  );
}
