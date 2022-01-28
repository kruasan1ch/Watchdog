import database.models
from database.database import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.router import router

database.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router=router)


