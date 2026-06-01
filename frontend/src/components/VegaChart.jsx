import React, { useEffect, useRef, useState } from 'react';
import { createChart, ColorType, CrosshairMode } from 'lightweight-charts';
import api from '../api';

const SYMBOLS = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK', 'SBIN', 'BHARTIARTL', 'ITC', 'ASIANPAINT', 'TITAN'];
const INTERVALS = ['1m', '5m', '15m', '30m', '1h', '1d'];

const VegaChart = () => {
  const containerRef = useRef();
  const chartRef = useRef();
  const seriesRef = useRef();
  const [symbol, setSymbol] = useState('RELIANCE');
  const [interval, setInterval] = useState('5m');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!containerRef.current) return;
    const chart = createChart(containerRef.current, {
      layout: { background: { type: ColorType.Solid, color: '#0C0C0E' }, textColor: '#888' },
      grid: { vertLines: { color: '#1a1a1e' }, horzLines: { color: '#1a1a1e' } },
      crosshair: { mode: CrosshairMode.Normal },
      rightPriceScale: { borderColor: '#1a1a1e' },
      timeScale: { borderColor: '#1a1a1e', timeVisible: true },
      width: containerRef.current.clientWidth,
      height: containerRef.current.clientHeight,
    });
    const series = chart.addCandlestickSeries({
      upColor: '#22c55e', downColor: '#ef4444',
      borderUpColor: '#22c55e', borderDownColor: '#ef4444',
      wickUpColor: '#22c55e', wickDownColor: '#ef4444',
    });
    chartRef.current = chart;
    seriesRef.current = series;
    const ro = new ResizeObserver(() => {
      if (containerRef.current) chart.applyOptions({ width: containerRef.current.clientWidth, height: containerRef.current.clientHeight });
    });
    ro.observe(containerRef.current);
    return () => { ro.disconnect(); chart.remove(); };
  }, []);

  useEffect(() => {
    if (!seriesRef.current) return;
    setLoading(true);
    api.get(`/api/ohlcv?symbol=${symbol}&interval=${interval}`)
      .then(({ data }) => {
        if (data && data.length) {
          const candles = data.map(d => ({ time: d.time, open: d.open, high: d.high, low: d.low, close: d.close }))
            .sort((a, b) => a.time - b.time);
          seriesRef.current.setData(candles);
          chartRef.current.timeScale().fitContent();
        }
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [symbol, interval]);

  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center gap-3 px-4 py-2 border-b border-border bg-surface/50">
        <select value={symbol} onChange={e => setSymbol(e.target.value)}
          className="bg-bg border border-border rounded-lg px-3 py-1.5 text-xs font-mono font-bold text-text outline-none focus:border-primary/40">
          {SYMBOLS.map(s => <option key={s}>{s}</option>)}
        </select>
        <div className="flex gap-1">
          {INTERVALS.map(iv => (
            <button key={iv} onClick={() => setInterval(iv)}
              className={`px-3 py-1.5 rounded-lg text-[10px] font-mono font-bold transition-all ${interval === iv ? 'bg-primary text-black' : 'text-text-dim hover:text-text hover:bg-surface'}`}>
              {iv}
            </button>
          ))}
        </div>
        {loading && <span className="text-[10px] font-mono text-primary animate-pulse ml-auto">LOADING...</span>}
      </div>
      <div ref={containerRef} className="flex-1" />
    </div>
  );
};

export default VegaChart;
