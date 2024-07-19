from sqlalchemy.orm import Session
from ..models import models, schemas


def create(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource


def read_all(db: Session):
    return db.query(models.Resource).all()


def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()


def update(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource:
        for key, value in resource.dict(exclude_unset=True).items():
            setattr(db_resource, key, value)
        db.commit()
        db.refresh(db_resource)
    return db_resource


def delete(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource:
        db.delete(db_resource)
        db.commit()
    return db_resource
