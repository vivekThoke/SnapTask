from fastapi import APIRouter
from app.core.config import settings

from app.utils.db_check import check_database

router = APIRouter()

@router.get("/health", tags=["Health"])
def health():
    print("Backend end point got hit")
    databse = "connected"
    
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
    
    