from typing import Sequence

from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models import models, schemas
from ..models.models import Recipe


def create(db: Session, recipe: schemas.RecipeCreate) -> models.Recipe:
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def read_all(db: Session) -> Sequence[Recipe]:
    return db.execute(select(models.Recipe)).scalars().all()


def read_one(db: Session, recipe_id: int) -> models.Recipe | None:
    return db.execute(select(models.Recipe).filter_by(id=recipe_id)).scalar_one_or_none()


def update(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate) -> models.Recipe | None:
    db_recipe = db.execute(select(models.Recipe).filter_by(id=recipe_id)).scalar_one_or_none()
    if db_recipe:
        update_data = recipe.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_recipe, key, value)
        db.commit()
        db.refresh(db_recipe)
    return db_recipe


def delete(db: Session, recipe_id: int) -> models.Recipe | None:
    db_recipe = db.execute(select(models.Recipe).filter_by(id=recipe_id)).scalar_one_or_none()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe
