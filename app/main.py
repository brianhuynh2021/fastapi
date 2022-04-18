from fastapi import FastAPI, Response, HTTPException, status, Depends
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

conn = psycopg2.connect(
    host="localhost",
    database="fastapi",
    user="postgres",
    password="54321",
    cursor_factory=RealDictCursor)


try:
    cursor = conn.cursor()
    print("Database connection was successfull!")
except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)


@app.get("/")
def root():
    return {"Project run well"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
