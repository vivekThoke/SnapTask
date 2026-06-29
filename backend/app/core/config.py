from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_env: str
    debug: bool
    
    database_host: str
    database_port: str
    database_name: str
    database_user: str
    database_password: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )

    @property
    def database_url(self): 
        return (
            f"postgresql://"
            f"{self.database_user}:"
            f"{self.database_password}@"
            f"{self.database_host}:"
            f"{self.database_port}/"
            f"{self.database_name}"
        )
    
    
settings = Settings()