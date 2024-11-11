from datetime import datetime
class DataPoint:
    def __init__(self, time: datetime, value: float):
        self.time = time
        self.value = value