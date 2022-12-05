from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app import schema
from app.dependencies import get_current_user
from app.repository import todo_repository

router = APIRouter(prefix="/api/v1/todos", tags=["todos"], )


@router.post('/', status_code=201)
def create(request: schema.Todo, response: Response, db: Session = Depends(get_db),
           current_user: schema.User = Depends(get_current_user)):
    return todo_repository.create(request, response, db, current_user)


@router.get("/", status_code=status.HTTP_200_OK)
def fetch_blogs(db: Session = Depends(get_db)):
    return todo_repository.get_all(db)


@router.get("/{todo_id}", status_code=200)
def show(todo_id: int,  response: Response, db: Session = Depends(get_db)):
    return todo_repository.show(todo_id, response, db)
