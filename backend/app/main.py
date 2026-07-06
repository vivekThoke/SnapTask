from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging

from app.exceptions.handlers import global_exception_handler

setup_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug  
)   

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.include_router(api_router)  