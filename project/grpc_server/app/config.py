import os
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    DATA_LOADER_TYPE: str = os.getenv("DATA_LOADER_TYPE", "csv")

    CSV_FILE_ADDRESS: str = os.getenv("CSV_FILE_ADDRESS", "meterusage.csv")

    INFLUXDB_URL: str = os.getenv("INFLUXDB_URL", "http://localhost:8086")
    INFLUXDB_TOKEN: str = os.getenv("INFLUXDB_TOKEN", "mytoken")
    INFLUXDB_ORG: str = os.getenv("INFLUXDB_ORG", "spectral")

settings = Config()