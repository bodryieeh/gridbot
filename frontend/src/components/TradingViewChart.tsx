import React, { useEffect, useRef } from 'react';
import { createChart, CandlestickData } from 'lightweight-charts';

interface Candle {
  time: string;
  open: number;
  high: number;
  low: number;
  close: number;
}

interface Props {
  data: Candle[];
}

const TradingViewChart: React.FC<Props> = ({ data }) => {
  const chartContainerRef = useRef<HTMLDivElement>(null);
  const seriesRef = useRef<any>(null);

  useEffect(() => {
    if (!chartContainerRef.current) return;

    const chart: any = createChart(chartContainerRef.current, {
      width: 800,
      height: 400,
    });

    const candleSeries = chart.addCandlestickSeries();
    seriesRef.current = candleSeries;

    const chartData: CandlestickData[] = data.map(item => ({
      time: item.time,
      open: item.open,
      high: item.high,
      low: item.low,
      close: item.close,
    }));

    candleSeries.setData(chartData);

    return () => {
      chart.remove();
    };
  }, [data]);

  return <div ref={chartContainerRef} />;
};

export default TradingViewChart;
