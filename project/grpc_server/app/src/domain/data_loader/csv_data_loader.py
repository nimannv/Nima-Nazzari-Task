import csv
from datetime import datetime, timezone
from typing import List
import math

from src.domain.data_loader.base import DataLoader
from src.domain.metric.data_point import DataPoint


class CSVDataLoader(DataLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_data_between(self, start_time: datetime, end_time: datetime) -> List[DataPoint]:
        data_points = []
        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                time = datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
                if start_time <= time < end_time:
                    value = float(row['meterusage'])
                    # NaN value is possible in CSV file
                    if math.isnan(value):
                        continue
                    data_points.append(DataPoint(time, value))
        return data_points
