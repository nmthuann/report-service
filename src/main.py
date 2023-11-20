

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

from src.modules.order.router import router as order_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency



@app.get("/")
async def home():
    return "Xin Chào mọi Người"

@app.get("/get-orders/", response_model=list[schemas.OrderSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


app.include_router(order_router, prefix="/order", tags=["Order"])