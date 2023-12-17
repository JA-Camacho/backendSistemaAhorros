from fastapi import FastAPI
from views.cliente_views import router as cliente_router
from database.database import database

app = FastAPI()

async def open_database_connection_pools():
    await database.connect()

async def close_database_connection_pools():
    await database.disconnect()

app.add_event_handler("startup", open_database_connection_pools)
app.add_event_handler("shutdown", close_database_connection_pools)
@app.get("/")
def read_root():
    return {"Hello": "World"}
app.include_router(cliente_router)
