from sqlalchemy.orm import Session

from . import models


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    print("Test get Order here!")
    return db.query(models.OrderEntity).order_by(models.OrderEntity.order_id).offset(skip).limit(limit).all()