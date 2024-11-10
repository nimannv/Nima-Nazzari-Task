from data.data_loader.csv_data_loader import CSVDataLoader
from data.data_loader.influxdb_data_loader import InfluxDBDataLoader
from data.data_loader.timescale_data_loader import TimescaleDBDataLoader

class DataLoaderFactory:
    @staticmethod
    def create_data_loader(loader_type, **kwargs):
        if loader_type == 'csv':
            return CSVDataLoader(kwargs['file_path'])
        elif loader_type == 'influxdb':
            return InfluxDBDataLoader(kwargs['host'], kwargs['port'], kwargs['database'])
        elif loader_type == 'timescale':
            return TimescaleDBDataLoader(kwargs['host'], kwargs['port'], kwargs['database'], kwargs['user'], kwargs['password'])
        else:
            raise ValueError(f"Unknown data loader type: {loader_type}")
