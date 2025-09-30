# backend/models.py

from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class BotConfig(Base):
    __tablename__ = "bot_configs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    exchange = Column(String, index=True)
    grid_size = Column(Integer)
    lower_price = Column(Float)
    upper_price = Column(Float)
    lot_size = Column(Float)

class PriceGrid(Base):
    __tablename__ = "price_grids"

    id = Column(Integer, primary_key=True, index=True)
    bot_id = Column(Integer, index=True)
    level = Column(Integer, index=True)
    price = Column(Float)
    side = Column(String)
    is_active = Column(Boolean, default=True)
