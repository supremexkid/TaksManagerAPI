from fastapi import FastAPI, HTTPException
from sqlalchemy.orm.session import Session
from app.models.task import Task
from app.crud.task import create_task, read_all_tasks, read_task
from app.database import SessionLocal, Base, engine
from app.schemas.task import TaskCreate, TaskResponse
from fastapi import Depends
from app.database import get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/tasks")
def handler(task_in:TaskCreate, db:Session = Depends(get_db), ) -> TaskResponse:
    return create_task(db, task_in)

@app.get("/tasks")
def task_list(db: Session = Depends(get_db)) -> list[TaskResponse]:
    read_func = read_all_tasks(db)
    return read_func

@app.get("/tasks/{task_id}")
def one_task(task_id: int,db: Session = Depends(get_db)) -> TaskResponse:
    read_func  = read_task(db, task_id)
    if read_func is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return read_func


