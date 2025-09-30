# backend/services/grid_service.py

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

class GridService:
    @staticmethod
    def create(db: Session, grid_in: schemas.PriceGridCreate) -> models.PriceGrid:
        grid = models.PriceGrid(**grid_in.dict())
        db.add(grid)
        db.commit()
        db.refresh(grid)
        return grid

    @staticmethod
    def list_by_bot(db: Session, bot_id: int) -> List[models.PriceGrid]:
        return db.query(models.PriceGrid).filter(models.PriceGrid.bot_id == bot_id).all()

    @staticmethod
    def delete(db: Session, grid_id: int) -> None:
        grid = db.query(models.PriceGrid).get(grid_id)
        if not grid:
            raise HTTPException(status_code=404, detail="Grid level not found")
        db.delete(grid)
        db.commit()
