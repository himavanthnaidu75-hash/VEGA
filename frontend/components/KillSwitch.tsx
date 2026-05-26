"use client";
import { Power } from "lucide-react";

export default function KillSwitch({ onTerminate }: { onTerminate: () => void }) {
  return (
    <button
      onClick={onTerminate}
      className="fixed bottom-8 right-8 w-16 h-16 bg-white border-2 border-red-500 rounded-full flex items-center justify-center text-red-500 hover:bg-red-500 hover:text-white transition-all shadow-xl group"
      title="EMERGENCY KILL SWITCH"
    >
      <Power size={32} className="group-hover:scale-110 transition-transform" />
    </button>
  );
}
