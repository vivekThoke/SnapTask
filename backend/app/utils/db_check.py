from sqlalchemy import text

from app.database.session import engine

def check_database():
    
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        
    return True