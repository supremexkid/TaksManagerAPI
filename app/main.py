from fastapi import FastAPI, HTTPException
from sqlalchemy.orm.session import Session
from app.models.task import Task
from app.crud.task import create_task, read_all_tasks, read_task, update_task, delete_task
from app.database import SessionLocal, Base, engine
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from fastapi import Depends
from app.database import get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/tasks")
def create_task_endpoint(task_in:TaskCreate, db:Session = Depends(get_db), ) -> TaskCreate:
    return create_task(db, task_in)

@app.get("/tasks")
def read_all_tasks_endpoint(db: Session = Depends(get_db)) -> list[TaskResponse]:
    read_func = read_all_tasks(db)
    return read_func

@app.get("/tasks/{task_id}")
def read_task_endpoint(task_id: int,db: Session = Depends(get_db)) -> TaskResponse:
    read_func  = read_task(db, task_id)
    if read_func is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return read_func


@app.patch("/tasks/{task_id}")
def update_task_endpoint(task_id: int,task_in: TaskUpdate, db: Session = Depends(get_db),) -> TaskResponse:
    read_func = update_task(db, task_id, task_in)
    if read_func is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return read_func

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db:Session = Depends(get_db),) -> dict[str, str]:
    read_func = delete_task(db, task_id)
    if read_func is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return {"message": "Задача удалена"}