import os


from fastapi import FastAPI
from mangum import Mangum
from starlette.requests import Request
from pyqldb.driver.qldb_driver import QldbDriver


my_app = FastAPI()


@my_app.get("/internal/ping")
async def get_root(request: Request):
    try:
        config = {} 
        config['MS_ORGANIZATIONS_API'] = os.environ.get('MS_ORGANIZATIONS_API', None)
        return {"message": "pong", 'config': config}
    except:
        return {'message': 'bad'}


lambda_handler = Mangum(app=my_app)