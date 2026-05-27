import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Terminal from './pages/Terminal';
import Scanner from './pages/Scanner';
import Analytics from './pages/Analytics';
import Config from './pages/Config';
import KillSwitch from './components/KillSwitch';
import ThreeBackground from './components/ThreeBackground';

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col relative">
        <ThreeBackground />

        {/* Top Bar */}
        <header className="fixed top-0 left-0 right-0 bg-white/80 backdrop-blur-md border-b border-gray-200 z-50 h-16 flex items-center px-8">
          <div className="flex-1 flex items-center space-x-8">
            <h1 className="text-xl font-bold tracking-tighter uppercase italic">Vega 2.0</h1>
            <div className="flex space-x-4 text-xs font-mono uppercase tracking-widest text-gray-500">
              <span>Daily PnL: <span className="text-success font-bold">+₹4,250.00</span></span>
              <span>Open: 3</span>
              <span className="flex items-center space-x-1">
                <div className="w-2 h-2 rounded-full bg-success"></div>
                <span>Running</span>
              </span>
            </div>
          </div>
          <KillSwitch />
        </header>

        {/* Navigation */}
        <nav className="fixed top-16 left-0 right-0 bg-white/50 backdrop-blur-sm border-b border-gray-100 z-40 h-12 flex items-center px-8">
          <div className="flex space-x-8 text-[10px] font-bold uppercase tracking-[0.2em] text-gray-400">
            <Link to="/" className="hover:text-ink transition-colors">Terminal</Link>
            <Link to="/scanner" className="hover:text-ink transition-colors">Scanner</Link>
            <Link to="/analytics" className="hover:text-ink transition-colors">Analytics</Link>
            <Link to="/config" className="hover:text-ink transition-colors">Config</Link>
          </div>
        </nav>

        {/* Main Content */}
        <main className="mt-28 p-8 flex-1 z-10">
          <Routes>
            <Route path="/" element={<Terminal />} />
            <Route path="/scanner" element={<Scanner />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/config" element={<Config />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
