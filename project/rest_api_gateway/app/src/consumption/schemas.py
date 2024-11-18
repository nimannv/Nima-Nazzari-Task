from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class data_point(BaseModel):
    value: Optional[float] = None # because there is NaN in our data
    time: datetime

class get_consumptions_res(BaseModel):
    data_points: List[data_point]