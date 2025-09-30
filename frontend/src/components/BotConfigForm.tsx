// src/components/BotConfigForm.tsx

import React from 'react';
import { useForm } from 'react-hook-form';

interface Config {
  name: string;
  symbol: string;
  min_price: number;
  max_price: number;
  levels: number;
  order_size: number;
}

const BotConfigForm: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Config>();

  const onSubmit = async (data: Config) => {
    const res = await fetch('/api/bot_config', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    if (!res.ok) {
      alert('Error saving config');
    } else {
      alert('Config saved');
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} style={{ maxWidth: 400 }}>
      <div>
        <label>Name</label>
        <input {...register('name', { required: true })} />
        {errors.name && <span>This field is required</span>}
      </div>
      <div>
        <label>Symbol</label>
        <input {...register('symbol', { required: true })} />
        {errors.symbol && <span>This field is required</span>}
      </div>
      <div>
        <label>Min Price</label>
        <input type="number" step="any" {...register('min_price', { valueAsNumber: true })} />
      </div>
      <div>
        <label>Max Price</label>
        <input type="number" step="any" {...register('max_price', { valueAsNumber: true })} />
      </div>
      <div>
        <label>Levels</label>
        <input type="number" {...register('levels', { valueAsNumber: true })} />
      </div>
      <div>
        <label>Order Size</label>
        <input type="number" step="any" {...register('order_size', { valueAsNumber: true })} />
      </div>
      <button type="submit">Save Bot Config</button>
    </form>
  );
};

export default BotConfigForm;
