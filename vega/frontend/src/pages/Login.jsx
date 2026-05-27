import React from 'react';
import { motion } from 'framer-motion';

const Login = () => {
  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="bg-white/40 backdrop-blur-xl border border-white/20 p-12 shadow-2xl z-20 w-full max-w-md"
      >
        <h2 className="text-4xl font-bold tracking-tighter uppercase mb-8 italic">Vega 2.0</h2>
        <div className="space-y-6">
          <input type="text" placeholder="Username" className="w-full bg-white/50 border-none px-4 py-3 focus:ring-2 focus:ring-secondary" />
          <input type="password" placeholder="Password" className="w-full bg-white/50 border-none px-4 py-3 focus:ring-2 focus:ring-secondary" />
          <button className="w-full bg-secondary text-ink font-bold py-4 uppercase tracking-[0.3em] hover:bg-black hover:text-white transition-all">
            Enter Terminal
          </button>
        </div>
        <p className="mt-8 text-[10px] text-gray-400 uppercase tracking-widest text-center">
          Secure Quantitative Access Node
        </p>
      </motion.div>
    </div>
  );
};

export default Login;
