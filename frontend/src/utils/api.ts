export async function fetchBotConfig(name: string) {
  const res = await fetch(`/api/bot_config/${name}`);
  if (!res.ok) throw new Error('Failed to load bot config');
  return await res.json();
}
