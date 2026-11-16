from requests import session
from sqlalchemy import select

from app.models.task import Task
from app.schemas.task import TaskCreate
from app.database import SessionLocal


def create_task(db,task_in)->TaskCreate:
    data = task_in.model_dump()
    db_task = Task(**data)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def read_all_tasks(db):
    all_tasks = db.scalars(select(Task)).all()
    return all_tasks


def read_task(db, task_id):
    one_task = db.scalars(select(Task).where(Task.id == task_id)).first()
    return one_task

def update_task(db, task_id, task_in):
    data = task_in.model_dump(exclude_unset=True)
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
        return None
    for key, value in data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

def delete_task(db, task_id):
    one_task = db.scalars(select(Task).where(Task.id == task_id)).first()

    if one_task is None:
        return None
    else:
        db.delete(one_task)

    db.commit()
    return True




