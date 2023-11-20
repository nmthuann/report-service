from typing import List
from . import service
from .schemas import OrderResponse
from fastapi import APIRouter, BackgroundTasks, Depends, Response, status
from sqlalchemy.orm import Session
from ...database import get_db

router = APIRouter()

@router.get("/completed", response_model=List[OrderResponse])
async def getOrderByCompletedStatus(db: Session = Depends(get_db)):
    return await service.get_completed_orders_this_year(db, 2023, 0, 100);