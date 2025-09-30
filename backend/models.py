from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
)
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class MarketData(Base):
    __tablename__ = "market_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, index=True, nullable=False)
    timestamp = Column(DateTime, index=True, default=datetime.datetime.utcnow)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)

class BotConfig(Base):
    __tablename__ = "bot_config"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)
    symbol = Column(String, index=True, nullable=False)
    min_price = Column(Float, nullable=False)
    max_price = Column(Float, nullable=False)
    levels = Column(Integer, nullable=False)
    order_size = Column(Float, nullable=False)
    params = Column(JSON, default={})  # для дополнительных AI-настроек
