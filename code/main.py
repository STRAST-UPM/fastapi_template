# external imports
from fastapi import FastAPI

# Routers imports
from src.routers.default_router import default_router
from src.routers.users_router import users_router
from src.routers.items_router import items_router

# needs to be created outside __main__ to be found by the executing command
app = FastAPI()

# Routers inclusion
app.include_router(router=default_router)
app.include_router(router=users_router)
app.include_router(router=items_router)
