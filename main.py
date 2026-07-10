from fastapi import FastAPI

from fastapi_project.database import Base, engine
from fastapi_project.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD Products")
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD app"}