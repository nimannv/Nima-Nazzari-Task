# import psycopg2
from datetime import datetime
from typing import List

from domain.data_loader.base import DataLoader
from domain.metric.data_point import DataPoint

class TimescaleDBDataLoader(DataLoader):
    def __init__(self, host, port, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

    def get_data_between(self, start_time: datetime, end_time: datetime) -> List[DataPoint]:
        raise Exception("Sorry, TimeScale data loader have not implemented yet")
