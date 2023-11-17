
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

#
# from fastapi import FastAPI
# # from pydantic import BaseModel
#
# app = FastAPI()
#
# @app.get("/")
# async def home():
#     return "Xin Chào mọi Người"

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home():
    return "Xin Chào mọi Người"

@app.get("/get-orders/", response_model=list[schemas.OrderSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders