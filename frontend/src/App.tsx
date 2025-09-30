// src/App.tsx
import React, { useEffect, useState } from 'react';
import './App.css';
import BotConfigForm from './components/BotConfigForm';
import PriceGridChart from './components/PriceGridChart';
import { fetchBotConfig } from './utils/api';

export interface Candle {
  time: string;
  open: number;
  high: number;
  low: number;
  close: number;
}

interface BotConfig {
  name: string;
  symbol: string;
  min_price: number;
  max_price: number;
  levels: number;
  order_size: number;
}

function App() {
  const [health, setHealth] = useState<string>('');
  const [candles, setCandles] = useState<Candle[]>([]);
  const [config, setConfig] = useState<BotConfig | null>(null);

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setHealth(data.status))
      .catch(() => setHealth('Error'));

    fetch('/api/market_data?symbol=BTCUSDT')
      .then(res => res.json())
      .then((data: any[]) => {
        const formatted = data.map(item => ({
          time: item.timestamp.split('T')[0],
          open: item.open,
          high: item.high,
          low: item.low,
          close: item.close,
        }));
        setCandles(formatted);
      });
    
    // Загрузка конфигурации бота с именем myBot
    fetchBotConfig('myBot')
      .then(cfg => setConfig(cfg))
      .catch(console.error);
  }, []);

  return (
    <div className="App" style={{ padding: 20 }}>
      <h1>GridBot Dashboard</h1>

      <section>
        <h2>Backend Status</h2>
        <p>{health}</p>
      </section>

      <section style={{ marginTop: 40 }}>
        <h2>Bot Configuration</h2>
        <BotConfigForm />
      </section>

      {config && candles.length > 0 && (
        <section style={{ marginTop: 40 }}>
          <h2>Price & Grid for {config.name}</h2>
          <PriceGridChart
            data={candles}
            gridLevels={config.levels}
            minPrice={config.min_price}
            maxPrice={config.max_price}
          />
        </section>
      )}
    </div>
  );
}

export default App;
