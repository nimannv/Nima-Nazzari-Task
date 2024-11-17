from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from domain.metric.data_point import DataPoint

class DataLoader(ABC):
    @abstractmethod
    def get_data_between(self, start_time: datetime, end_time: datetime) -> List[DataPoint]:
        pass