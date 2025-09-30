# backend/schemas.py

from pydantic import BaseModel

# BotConfig schemas
class BotConfigBase(BaseModel):
    name: str
    exchange: str
    grid_size: int
    lower_price: float
    upper_price: float
    lot_size: float

class BotConfigCreate(BotConfigBase):
    pass

class BotConfig(BotConfigBase):
    id: int

    class Config:
        from_attributes = True

# PriceGrid schemas
class PriceGridBase(BaseModel):
    bot_id: int
    level: int
    price: float
    side: str

class PriceGridCreate(PriceGridBase):
    pass

class PriceGrid(PriceGridBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
