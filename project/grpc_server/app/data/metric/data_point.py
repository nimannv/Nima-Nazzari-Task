from datetime import datetime
from dataclasses import dataclass

@dataclass
class DataPoint:
    def __init__(self, time: datetime, value: float):
        self.time = time
        self.value = value