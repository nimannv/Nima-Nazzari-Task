from datetime import datetime
from data.data_loader.data_loader_factory import DataLoaderFactory
from data.metric.metric import Metric

def test_csv():
    
    csv_loader = DataLoaderFactory.create_data_loader(
        'csv',
        file_path='meterusage.csv'
    )
    metric_csv = Metric(csv_loader)
    
    start_time = datetime.strptime("2019-01-01 01:00:00", '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime("2019-01-01 02:00:00", '%Y-%m-%d %H:%M:%S')

    csv_data = metric_csv.get_data_between(start_time, end_time)
    for data in csv_data:
        print(data.time, data.value)














