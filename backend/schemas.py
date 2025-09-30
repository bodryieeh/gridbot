# schemas.py

from pydantic import BaseModel
from datetime import datetime

# Схема для создания MarketData
class MarketDataCreate(BaseModel):
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    class Config:
        from_attributes = True

# Схема для BotConfig
class BotConfigBase(BaseModel):
    name: str
    symbol: str
    min_price: float
    max_price: float
    levels: int
    order_size: float

class BotConfigCreate(BotConfigBase):
    pass

class BotConfigRead(BotConfigBase):
    id: int
    params: dict

    class Config:
        from_attributes = True
