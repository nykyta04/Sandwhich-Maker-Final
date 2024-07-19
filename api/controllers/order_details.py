from typing import Sequence

from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models import models, schemas
from ..models.models import Recipe


def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(**order_detail.dict())
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id: int):
    return db.execute(
        select(models.OrderDetail).filter_by(id=models.OrderDetail.id == order_detail_id)).scalar_one_or_none()


def update(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_detail = db.execute(
        select(models.OrderDetail).filter_by(id=models.OrderDetail.id == order_detail_id)).scalar_one_or_none()

    if db_order_detail:
        for key, value in order_detail.dict(exclude_unset=True).items():
            setattr(db_order_detail, key, value)
        db.commit()
        db.refresh(db_order_detail)
    return db_order_detail


def delete(db: Session, order_detail_id: int):
    db_order_detail = db.execute(
        select(models.OrderDetail).filter_by(id=models.OrderDetail.id == order_detail_id)).scalar_one_or_none()
    if db_order_detail:
        db.delete(db_order_detail)
        db.commit()
    return db_order_detail
