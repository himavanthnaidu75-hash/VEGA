import React, { useEffect, useRef, useState, useCallback } from 'react';
import { createChart, ColorType, CrosshairMode } from 'lightweight-charts';
import api from '../api';

// Full NSE 500 most-traded symbols
const NSE_SYMBOLS = [
  'RELIANCE','TCS','HDFCBANK','INFY','ICICIBANK','SBIN','BHARTIARTL','ITC',
  'ASIANPAINT','TITAN','KOTAKBANK','LT','AXISBANK','HCLTECH','BAJFINANCE',
  'WIPRO','ULTRACEMCO','MARUTI','SUNPHARMA','TATAMOTORS','NTPC','POWERGRID',
  'TATASTEEL','ADANIENT','ADANIPORTS','BAJAJFINSV','TECHM','HINDALCO','ONGC',
  'JSWSTEEL','GRASIM','DIVISLAB','DRREDDY','EICHERMOT','HEROMOTOCO','CIPLA',
  'APOLLOHOSP','NESTLEIND','COALINDIA','BPCL','BRITANNIA','SBILIFE','HDFCLIFE',
  'INDUSINDBK','VEDL','TATACONSUM','PIDILITIND','SIEMENS','HAVELLS','GODREJCP',
  'DABUR','MARICO','COLPAL','BERGEPAINT','WHIRLPOOL','VOLTAS','BLUESTARCO',
  'BANDHANBNK','FEDERALBNK','IDFCFIRSTB','RBLBANK','YESBANK','PNB','CANBK',
  'BANKBARODA','UNIONBANK','MAHABANK','IDBI','LICHSGFIN','BAJAJ-AUTO','TVSMOTORS',
  'M&M','ESCORTS','ASHOKLEY','TVSMOTOR','MOTHERSON','BOSCHLTD','EXIDEIND',
  'AMARAJABAT','BALKRISIND','APOLLOTYRE','MRF','CEATLTD','ZOMATO','NYKAA',
  'PAYTM','POLICYBZR','DELHIVERY','CARTRADE','EASEMYTRIP','IRCTC','INDIGO',
  'SPICEJET','INTERGLOBE','GMRINFRA','ADANIGREEN','TATAPOWER','ADANITRANS',
  'TORNTPOWER','CESC','JPPOWER','NHPC','SJVN','RECLTD','PFC','IRFC','HUDCO',
  'OBEROIRLTY','DLF','GODREJPROP','PRESTIGE','PHOENIXLTD','SOBHA','BRIGADE',
  'MFSL','CHOLAFIN','MUTHOOTFIN','MANAPPURAM','M&MFIN','SRTRANSFIN','L&TFH',
  'IIFL','ICICIGI','BAJAJHLDNG','MAX','STARHEALTH','NIACL','GICRE','LICI',
  'AUROPHARMA','LUPIN','TORNTPHARM','ALKEM','IPCA','ABBOTINDIA','PFIZER',
  'GLAXO','BIOCON','LAURUSLABS','GRANULES','IPCALAB','SUVEN','NATCOPHARM',
  'HINDUNILVR','PGHH','EMAMILTD','GILLETTE','VGUARD','SYMPHONY','CROMPTON',
  'ORIENTELEC','POLYCAB','KPITTECH','LTTS','PERSISTENT','COFORGE','MPHASIS',
  'HEXAWARE','ZENSARTECH','NIITTECH','OFSS','INFOEDGE','JUSTDIAL','INDIAMART',
  'MATRIMONY','TEAMLEASE','QUESS','SIS','CDSL','BSE','MCX','CAMS','KFINTECH',
  'NAUKRI','MAKEMYTRIP','RATEGAIN','AFFLE','NAZARA','NETWEB','TATAELXSI',
  'ZENTEC','CYIENT','MASTEK','BIRLASOFT','SONATSOFTW','MINDTREE','MPSLTD',
];

const INTERVALS = ['1m', '5m', '15m', '30m', '1h', '1d'];

const VegaChart = () => {
  const containerRef = useRef();
  const chartRef = useRef();
  const seriesRef = useRef();
  const [symbol, setSymbol] = useState('RELIANCE');
  const [searchQuery, setSearchQuery] = useState('RELIANCE');
  const [showDropdown, setShowDropdown] = useState(false);
  const [interval, setInterval] = useState('5m');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const filteredSymbols = NSE_SYMBOLS.filter(s =>
    s.toLowerCase().includes(searchQuery.toLowerCase())
  ).slice(0, 20);

  useEffect(() => {
    if (!containerRef.current) return;
    const chart = createChart(containerRef.current, {
      layout: { background: { type: ColorType.Solid, color: '#0C0C0E' }, textColor: '#888' },
      grid: { vertLines: { color: '#1a1a1e' }, horzLines: { color: '#1a1a1e' } },
      crosshair: { mode: CrosshairMode.Normal },
      rightPriceScale: { borderColor: '#1a1a1e' },
      timeScale: { borderColor: '#1a1a1e', timeVisible: true, secondsVisible: false },
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
      if (containerRef.current && chartRef.current)
        chartRef.current.applyOptions({ width: containerRef.current.clientWidth, height: containerRef.current.clientHeight });
    });
    ro.observe(containerRef.current);
    return () => { ro.disconnect(); chartRef.current?.remove(); };
  }, []);

  useEffect(() => {
    if (!seriesRef.current) return;
    setLoading(true);
    setError(null);
    api.get(`/api/ohlcv?symbol=${symbol}&interval=${interval}`)
      .then(({ data }) => {
        if (data && data.length) {
          // Deduplicate by time and sort ascending
          const seen = new Set();
          const candles = data
            .map(d => ({ time: d.time, open: d.open, high: d.high, low: d.low, close: d.close }))
            .filter(d => { if (seen.has(d.time)) return false; seen.add(d.time); return true; })
            .sort((a, b) => a.time - b.time);
          seriesRef.current.setData(candles);
          chartRef.current.timeScale().fitContent();
        } else {
          setError('No data available for this symbol/interval');
        }
      })
      .catch(() => setError('Failed to load chart data'))
      .finally(() => setLoading(false));
  }, [symbol, interval]);

  const selectSymbol = (s) => {
    setSymbol(s);
    setSearchQuery(s);
    setShowDropdown(false);
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center gap-3 px-4 py-2 border-b border-border bg-surface/50 flex-wrap">
        {/* Searchable symbol input */}
        <div className="relative">
          <input
            value={searchQuery}
            onChange={e => { setSearchQuery(e.target.value); setShowDropdown(true); }}
            onFocus={() => setShowDropdown(true)}
            onBlur={() => setTimeout(() => setShowDropdown(false), 150)}
            placeholder="Search NSE symbol..."
            className="bg-bg border border-border rounded-lg px-3 py-1.5 text-xs font-mono font-bold text-text outline-none focus:border-primary/40 w-40"
          />
          {showDropdown && filteredSymbols.length > 0 && (
            <div className="absolute top-full left-0 mt-1 w-48 bg-surface border border-border rounded-xl shadow-2xl z-50 max-h-48 overflow-y-auto">
              {filteredSymbols.map(s => (
                <div key={s} onMouseDown={() => selectSymbol(s)}
                  className="px-4 py-2 text-xs font-mono font-bold text-text hover:bg-primary/10 hover:text-primary cursor-pointer transition-colors">
                  {s}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Interval buttons */}
        <div className="flex gap-1">
          {INTERVALS.map(iv => (
            <button key={iv} onClick={() => setInterval(iv)}
              className={`px-3 py-1.5 rounded-lg text-[10px] font-mono font-bold transition-all ${interval === iv ? 'bg-primary text-black' : 'text-text-dim hover:text-text hover:bg-surface'}`}>
              {iv}
            </button>
          ))}
        </div>

        <div className="ml-auto flex items-center gap-3">
          {loading && <span className="text-[10px] font-mono text-primary animate-pulse">LOADING...</span>}
          {error && <span className="text-[10px] font-mono text-red-400">{error}</span>}
          <span className="text-[10px] font-mono text-text-faint">NSE:{symbol}</span>
        </div>
      </div>
      <div ref={containerRef} className="flex-1" />
    </div>
  );
};

export default VegaChart;