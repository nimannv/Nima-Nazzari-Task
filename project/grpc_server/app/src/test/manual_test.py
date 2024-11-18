from datetime import datetime, timezone
from src.domain.data_loader.data_loader_factory import DataLoaderFactory
from src.domain.metric.metric_use_case import MetricUseCase

def csv_test():
    
    csv_loader = DataLoaderFactory.create_csv_loader('meterusage.csv')
    metric_use_case = MetricUseCase(csv_loader)
    
    start_time = datetime.strptime("2019-01-01 01:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime("2019-01-01 02:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)

    data_points = metric_use_case.get_data_between(start_time, end_time)
    for dp in data_points:
        print(dp.time, dp.value)

def influx_test():
    data_loader = DataLoaderFactory.create_influxdb_loader('http://localhost:8086', 'mytoken', 'spectral')
    metric_use_case = MetricUseCase(data_loader)
    
    start_time = datetime.strptime("2019-01-01 01:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime("2019-01-01 02:00:00", '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)

    data_points = metric_use_case.get_data_between(start_time, end_time)
    for dp in data_points:
        print(dp.time, dp.value)
        















