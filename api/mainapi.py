from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import path

app = FastAPI()
app.include_router(path)

app.mount("/", StaticFiles(directory=r"..\physics-Website", html=True))
