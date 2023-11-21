from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from src import models
from src.common.Enums.enums import OrderStatus



def get_orders(db: Session, skip: int = 0, limit: int = 100):
    print("Test get Order here!")
    return db.query(models.OrderEntity).order_by(models.OrderEntity.order_id).offset(skip).limit(limit).all()

async def get_completed_orders_this_year(db: Session, year: int, skip: int = 0, limit: int = 100)-> List[models.OrderEntity]:
    start_date = datetime(year, 1, 1, 0, 0, 0)
    end_date = datetime(year + 1, 1, 1, 0, 0, 0)

    # Lọc theo trạng thái là "completed" và năm tạo là năm hiện tại
    find_orders =  (
        db.query(models.OrderEntity)
        .filter(models.OrderEntity.status == OrderStatus.Completed.value)
        .filter(models.OrderEntity.created_at.between(start_date, end_date))
        .order_by(models.OrderEntity.order_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return find_orders
