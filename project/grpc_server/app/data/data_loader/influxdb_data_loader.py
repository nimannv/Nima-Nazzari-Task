from influxdb_client import InfluxDBClient
from datetime import datetime
from typing import List

from data.data_loader.base import DataLoader
from data.metric.data_point import DataPoint

class InfluxDBDataLoader(DataLoader):
    def __init__(self, url: str, token: str, org: str):
        self.client = InfluxDBClient(
            url=url,
            token=token,
            org=org
        )
    
    def get_data_between(self, start_time: datetime, end_time: datetime) -> List[DataPoint]:
        
        # Convert datetime to RFC3339 format
        start_time_str = start_time.isoformat()
        end_time_str = end_time.isoformat()

        query_api = self.client.query_api()

        query = f'''
            from(bucket: "spectral")
            |> range(start: {start_time_str}, stop: {end_time_str})
            |> filter(fn: (r) => r["_measurement"] == "meterusage")
            |> filter(fn: (r) => r["_field"] == "meterusage")
        '''

        results = query_api.query(query)

        data_points = []
        for table in results:
            for record in table.records:
                time = record.get_time()
                value = record.get_value()
                data_points.append(DataPoint(time, value))
        
        return data_points
