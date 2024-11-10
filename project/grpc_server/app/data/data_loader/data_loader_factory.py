from data.data_loader.csv_data_loader import CSVDataLoader
from data.data_loader.influxdb_data_loader import InfluxDBDataLoader
from data.data_loader.timescale_data_loader import TimescaleDBDataLoader

class DataLoaderFactory:

    @staticmethod
    def create_csv_loader(file_path: str) -> CSVDataLoader:
        """Creates and returns a CSVDataLoader."""
        return CSVDataLoader(file_path)

    @staticmethod
    def create_influxdb_loader(host: str, port: int, database: str) -> InfluxDBDataLoader:
        """Creates and returns an InfluxDBDataLoader."""
        return InfluxDBDataLoader(host, port, database)

    @staticmethod
    def create_timescale_loader(
            host: str,
            port: int,
            database: str,
            user: str,
            password: str
    ) -> TimescaleDBDataLoader:
        """Creates and returns a TimescaleDBDataLoader."""
        return TimescaleDBDataLoader(host, port, database, user, password)