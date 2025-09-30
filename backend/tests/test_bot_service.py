# backend/tests/test_bot_service.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Важно: импортировать Base и модели из вашего backend
from database import Base, engine as _engine
import models                        # <-- здесь регистрируются модели
from services.bot_service import BotService
from schemas import BotConfigCreate

# Настройка in-memory БД
ENGINE = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False}
)
SessionTesting = sessionmaker(
    autocommit=False, autoflush=False, bind=ENGINE
)

@pytest.fixture(scope="module")
def db():
    # Импорт моделей перед create_all обеспечивает их регистрацию
    Base.metadata.create_all(bind=ENGINE)
    session = SessionTesting()
    yield session
    session.close()

def test_create_and_get_bot(db):
    bot_in = BotConfigCreate(
        name="testbot",
        exchange="Bybit",
        grid_size=3,
        lower_price=100.0,
        upper_price=200.0,
        lot_size=0.1
    )
    created = BotService.create(db, bot_in)
    assert created.id == 1
    fetched = BotService.get(db, created.id)
    assert fetched.name == "testbot"

def test_list_bots(db):
    bots = BotService.list(db)
    assert len(bots) == 1

def test_update_bot(db):
    bot_in = BotConfigCreate(
        name="updated",
        exchange="Binance",
        grid_size=4,
        lower_price=90.0,
        upper_price=210.0,
        lot_size=0.2
    )
    updated = BotService.update(db, 1, bot_in)
    assert updated.name == "updated"
    assert updated.exchange == "Binance"

def test_delete_bot(db):
    BotService.delete(db, 1)
    with pytest.raises(Exception):
        BotService.get(db, 1)
