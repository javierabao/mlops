from fastapi import FastAPI
from utils import return_one

app = FastAPI()


@app.get("/")
async def root():
    return return_one()
