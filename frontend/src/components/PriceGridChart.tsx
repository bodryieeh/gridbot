// src/components/PriceGridChart.tsx
import React from 'react';
import {
  ResponsiveContainer,
  ComposedChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ReferenceLine,
} from 'recharts';

interface Candle {
  time: string;
  open: number;
  high: number;
  low: number;
  close: number;
}

interface Props {
  data: Candle[];
  gridLevels: number;
  minPrice: number;
  maxPrice: number;
}

const PriceGridChart: React.FC<Props> = ({
  data,
  gridLevels,
  minPrice,
  maxPrice,
}) => {
  const step = (maxPrice - minPrice) / (gridLevels - 1);
  const gridLines = Array.from({ length: gridLevels }, (_, i) => minPrice + step * i);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <ComposedChart data={data}>
        <CartesianGrid stroke="#f5f5f5" />
        <XAxis dataKey="time" />
        <YAxis domain={[minPrice, maxPrice]} />
        <Tooltip />
        <Line type="monotone" dataKey="close" stroke="#8884d8" dot={false} />
        {gridLines.map((price, idx) => (
          <ReferenceLine
            key={idx}
            y={price}
            stroke="red"
            strokeDasharray="3 3"
          />
        ))}
      </ComposedChart>
    </ResponsiveContainer>
  );
};

export default PriceGridChart;
