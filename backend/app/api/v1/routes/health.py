import logging

from fastapi import APIRouter
from app.core.config import settings

from app.utils.db_check import check_database

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/health", tags=["Health"])
def health():
    databse = "connected"
    logger.info("Health endpoint was called")
    
    try: 
        check_database()            
    except Exception as e:
        print(e)
        databse = "disconnected"
    
    return {
        "status": "healthy",
        "database": databse,
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env 
    }
    
    