from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, AsyncSessionLocal
from models import Base, MarketData, BotConfig
from schemas import MarketDataCreate, BotConfigCreate, BotConfigRead
from datetime import datetime

app = FastAPI()

# Dependency: выдаёт сессию БД
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Создание всех таблиц при старте приложения
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/api/health")
def health():
    return {"status": "ok"}

# -----------------------
# MarketData endpoints
# -----------------------

@app.post("/api/market_data")
async def create_market_data(
    data: MarketDataCreate,
    db: AsyncSession = Depends(get_db)
):
    md = MarketData(**data.dict())
    db.add(md)
    await db.commit()
    await db.refresh(md)
    return md

@app.get("/api/market_data")
async def read_market_data(
    symbol: str,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(MarketData)
        .where(MarketData.symbol == symbol)
        .order_by(MarketData.timestamp.desc())
        .limit(limit)
    )
    items = result.scalars().all()
    return items[::-1]  # вернуть в порядке возрастания времени

# -----------------------
# BotConfig endpoints
# -----------------------

@app.post("/api/bot_config", response_model=BotConfigRead)
async def create_bot_config(
    cfg: BotConfigCreate,
    db: AsyncSession = Depends(get_db)
):
    bot = BotConfig(**cfg.dict())
    db.add(bot)
    await db.commit()
    await db.refresh(bot)
    return bot

@app.get("/api/bot_config/{name}", response_model=BotConfigRead)
async def read_bot_config(
    name: str,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(BotConfig).where(BotConfig.name == name)
    )
    bot = result.scalar_one_or_none()
    if not bot:
        raise HTTPException(status_code=404, detail="BotConfig not found")
    return bot
