# backend/services/bot_service.py

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

class BotService:
    @staticmethod
    def create(db: Session, bot_in: schemas.BotConfigCreate) -> models.BotConfig:
        db_bot = models.BotConfig(**bot_in.dict())
        db.add(db_bot)
        db.commit()
        db.refresh(db_bot)
        return db_bot

    @staticmethod
    def get(db: Session, bot_id: int) -> models.BotConfig:
        bot = db.query(models.BotConfig).get(bot_id)
        if not bot:
            raise HTTPException(status_code=404, detail="Bot not found")
        return bot

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100) -> List[models.BotConfig]:
        return db.query(models.BotConfig).offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, bot_id: int, bot_in: schemas.BotConfigCreate) -> models.BotConfig:
        bot = BotService.get(db, bot_id)
        for key, value in bot_in.dict().items():
            setattr(bot, key, value)
        db.commit()
        db.refresh(bot)
        return bot

    @staticmethod
    def delete(db: Session, bot_id: int) -> None:
        bot = BotService.get(db, bot_id)
        db.delete(bot)
        db.commit()
