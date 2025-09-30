# backend/main.py

from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
import models
import schemas
from services.bot_service import BotService
from services.grid_service import GridService

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD для BotConfig
@app.post("/bots/", response_model=schemas.BotConfig)
def create_bot(bot_in: schemas.BotConfigCreate, db: Session = Depends(get_db)):
    return BotService.create(db, bot_in)

@app.get("/bots/", response_model=List[schemas.BotConfig])
def read_bots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return BotService.list(db, skip, limit)

@app.get("/bots/{bot_id}", response_model=schemas.BotConfig)
def read_bot(bot_id: int, db: Session = Depends(get_db)):
    return BotService.get(db, bot_id)

@app.patch("/bots/{bot_id}", response_model=schemas.BotConfig)
def update_bot(bot_id: int, bot_in: schemas.BotConfigCreate, db: Session = Depends(get_db)):
    return BotService.update(db, bot_id, bot_in)

@app.delete("/bots/{bot_id}", status_code=204)
def delete_bot(bot_id: int, db: Session = Depends(get_db)):
    BotService.delete(db, bot_id)

# CRUD для PriceGrid
@app.post("/grids/", response_model=schemas.PriceGrid)
def create_grid(grid_in: schemas.PriceGridCreate, db: Session = Depends(get_db)):
    return GridService.create(db, grid_in)

@app.get("/bots/{bot_id}/grids/", response_model=List[schemas.PriceGrid])
def get_grids(bot_id: int, db: Session = Depends(get_db)):
    return GridService.list_by_bot(db, bot_id)

@app.delete("/grids/{grid_id}", status_code=204)
def delete_grid(grid_id: int, db: Session = Depends(get_db)):
    GridService.delete(db, grid_id)
