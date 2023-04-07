from pymongo import MongoClient
from ..models.viewmodels import Tasks
from bson import ObjectId
from typing import Union, Optional, Dict, List
import os

class MongoDbRepository:
    def __init__(self):
        #uri = 'mongodb://localhost:27017'
        uri = os.environ['uri_mongo']
        client = MongoClient(uri)
        db = client['tasksWeb']
        self.tasks = db['tasks']

    def CreatTask(self, task) -> str:
        _id = self.tasks.insert_one(task.toDict()).inserted_id
        task.id = str(_id)
        return {'mensagem': 'Task Created'}

    def ShowTask(self) -> List:
        tasks = self.tasks.find()
        return list(map(Tasks.fromDict,tasks))

    def ShowById(self, id) -> Optional[Union[Tasks, Dict[str, str]]]:
        if len(id) != 24:
            return {'mensagem':'quantidade de carcteres invalida'}
        filter = {"_id": ObjectId(id)}
        task_found = self.tasks.find_one(filter)
        if task_found :
            return Tasks.fromDict(task_found)
        return {'mensagem','user not found'}

    def RemoveTask(self,id ) -> None:
        if len(id) != 24:
            return {'mensagem':'quantidade de carcteres invalida'}
        filter = {"_id": ObjectId(id)}
        task_found = self.tasks.find_one(filter)
        if task_found :
            self.tasks.delete_one(task_found)
            return {'mensagem':'task removed'}
        return {'mensagem','user not found'}
    def UpdateTask(self,id,task) -> Optional[Tasks]:
        filter = {'_id':ObjectId(id)}
        self.tasks.update_one(filter,{'$set':task.toDict()})
        task.id = id 
        return task   