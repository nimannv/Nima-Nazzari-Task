import csv
from datetime import datetime
from typing import List
import math

from data.data_loader.base import DataLoader
from data.metric.data_point import DataPoint


class CSVDataLoader(DataLoader):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data_between(self, start_time: datetime, end_time: datetime) -> List[DataPoint]:
        data_points = []
        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                time = datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S')
                if start_time <= time <= end_time:
                    value = float(row['meterusage'])
                    if math.isnan(value):
                        value = None
                    data_points.append(DataPoint(time, value))
        return data_points
