import React from 'react';

const Terminal = () => {
  return (
    <div className="grid grid-cols-12 gap-8">
      {/* Chart Panel */}
      <div className="col-span-8 h-[60vh] bg-ink rounded-none shadow-2xl relative overflow-hidden">
        <div className="absolute top-4 left-4 text-white text-[10px] font-mono opacity-50 uppercase tracking-tighter">
          NIFTY 50 • 5M • Dhan Feed
        </div>
        <div className="flex items-center justify-center h-full text-gray-700 font-mono italic">
          [ Lightweight Chart Panel ]
        </div>
      </div>

      {/* Signals / Scanner */}
      <div className="col-span-4 space-y-4">
        <h3 className="text-xs font-bold uppercase tracking-widest text-gray-400">Live Signals</h3>
        <div className="bg-white border border-gray-100 p-6 shadow-sm">
          <div className="flex justify-between items-start">
            <div>
              <span className="text-[10px] bg-secondary px-2 py-0.5 font-bold uppercase">EMA Confluence</span>
              <h4 className="text-lg font-bold mt-1 font-mono tracking-tight">RELIANCE • BUY</h4>
            </div>
            <div className="text-right">
              <span className="text-[10px] text-gray-400 block uppercase">ICT Score</span>
              <span className="text-lg font-bold font-mono">85/100</span>
            </div>
          </div>
          <div className="mt-4 flex justify-between text-xs font-mono">
            <span>Entry: 2854.50</span>
            <span className="text-danger">SL: 2840.00</span>
            <span className="text-success">TP: 2900.00</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Terminal;
