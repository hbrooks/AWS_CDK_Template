import os


from fastapi import FastAPI
from mangum import Mangum
from starlette.requests import Request


my_app = FastAPI()


@my_app.get("/internal/ping")
async def get_root(request: Request):
    try:
        config = {} 
        return {'is_healthy': True, 'config': config}
    except:
        return {'is_healthy': False}


lambda_handler = Mangum(app=my_app)