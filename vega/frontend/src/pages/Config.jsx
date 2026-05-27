import React, { useState } from 'react';

const Config = () => {
  const [primary, setPrimary] = useState('#F7F7F5');
  const [secondary, setSecondary] = useState('#F5C518');

  const updateTheme = (p, s) => {
    setPrimary(p);
    setSecondary(s);
    document.documentElement.style.setProperty('--color-primary', p);
    document.documentElement.style.setProperty('--color-secondary', s);
  };

  return (
    <div className="max-w-4xl space-y-12">
      <section>
        <h2 className="text-2xl font-bold uppercase tracking-tight mb-8">Theme Customization</h2>
        <div className="grid grid-cols-2 gap-8">
          <div className="space-y-4 p-8 bg-white border border-gray-100 shadow-sm">
            <h3 className="text-xs font-bold uppercase text-gray-400">Color Pickers</h3>
            <div className="flex items-center space-x-4">
              <input type="color" value={primary} onChange={(e) => updateTheme(e.target.value, secondary)} />
              <label className="text-sm font-mono uppercase">Primary</label>
            </div>
            <div className="flex items-center space-x-4">
              <input type="color" value={secondary} onChange={(e) => updateTheme(primary, e.target.value)} />
              <label className="text-sm font-mono uppercase">Secondary</label>
            </div>
          </div>
          <div className="space-y-4 p-8 bg-white border border-gray-100 shadow-sm">
            <h3 className="text-xs font-bold uppercase text-gray-400">Presets</h3>
            <div className="flex flex-col space-y-2">
              <button onClick={() => updateTheme('#F7F7F5', '#F5C518')} className="text-left text-sm font-mono uppercase hover:text-secondary">Electric Yellow (Default)</button>
              <button onClick={() => updateTheme('#F7F7F5', '#0A0F2C')} className="text-left text-sm font-mono uppercase hover:text-secondary">Deep Ink Blue</button>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Config;
