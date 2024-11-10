from influxdb import InfluxDBClient
from datetime import datetime
from typing import List

from data.data_loader.base import DataLoader
from data.metric.data_point import DataPoint

class InfluxDBDataLoader(DataLoader):
    def __init__(self, host, port, database):
        self.client = InfluxDBClient(host=host, port=port, database=database)

    def get_data_between(self, start_time: datetime, end_time: datetime) -> List[DataPoint]:
        raise Exception("Sorry, Influx data loader have not implemented yet")
