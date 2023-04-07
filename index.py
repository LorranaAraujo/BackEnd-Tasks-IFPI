from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.controller import task_controller
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

#origins = ['http://127.0.0.1:8000','http://127.0.0.1:5500','http://localhost:8000','https://lorranaaraujo.github.io/Tasks-JS-IFPI/']
origins = ['*']



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(task_controller.routes,
                   prefix=task_controller.prefix)