from datetime import datetime, timezone
from data.data_loader.data_loader_factory import DataLoaderFactory
from data.metric.metric import Metric

def csv_test():
    
    csv_loader = DataLoaderFactory.create_csv_loader('meterusage.csv')
    metric = Metric(csv_loader)
    
    start_time = datetime.strptime("2019-01-01 01:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime("2019-01-01 02:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)

    csv_data = metric.get_data_between(start_time, end_time)
    for data in csv_data:
        print(data.time, data.value)

def influx_test():
    data_loader = DataLoaderFactory.create_influxdb_loader('http://localhost:8086', 'mytoken', 'spectral')
    metric = Metric(data_loader)
    
    start_time = datetime.strptime("2019-01-01 01:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime("2019-01-01 02:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)

    csv_data = metric.get_data_between(start_time, end_time)
    for data in csv_data:
        print(data.time, data.value)
        















