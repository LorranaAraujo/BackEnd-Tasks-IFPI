from fastapi import APIRouter, status
from app.models.viewmodels import Tasks
from ...repository.mongoDB_repository import MongoDbRepository


routes = APIRouter()
prefix = '/tasks'

@routes.post('/',status_code=status.HTTP_201_CREATED)
async def create_task(task:Tasks):
    return MongoDbRepository().CreatTask(task)

@routes.get('/', status_code=status.HTTP_200_OK)
async def show_task():
    return MongoDbRepository().ShowTask()

@routes.get('/{id}',status_code=status.HTTP_200_OK)
async def show_by_id(id:str):
    return MongoDbRepository().ShowById(id)

@routes.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_task (id:str):
    return MongoDbRepository().RemoveTask(id)


@routes.put('/{id}')
async def update_task(id:str, task:Tasks):
    return MongoDbRepository().UpdateTask(id, task)