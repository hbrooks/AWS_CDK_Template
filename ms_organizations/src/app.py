import os


from fastapi import FastAPI
from mangum import Mangum
from starlette.requests import Request
from pyqldb.driver.qldb_driver import QldbDriver


my_app = FastAPI()


@my_app.get("/internal/ping")
async def get_root(request: Request):
    try:
        qldb_name = os.environ.get('QLDB_NAME', None)
        qldb_driver = QldbDriver(ledger_name=qldb_name)
        for table in qldb_driver.list_tables():
            print(table)
        config = {} 
        config['QLDB_NAME'] = qldb_name      
        return {"message": "pong", 'config': config}
    except:
        return {'message': 'bad'}


lambda_handler = Mangum(app=my_app)