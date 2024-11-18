import unittest
from unittest.mock import patch, mock_open
from datetime import datetime, timezone
from src.domain.data_loader.csv_data_loader import CSVDataLoader
from src.domain.metric.data_point import DataPoint


class TestCSVDataLoader(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=""
    )
    def test_empty_file(self, mock_file):
        # given
        start_time = datetime(2023, 1, 1, tzinfo=timezone.utc)
        end_time = datetime(2023, 1, 2, tzinfo=timezone.utc)
        expected = []
        loader = CSVDataLoader("dummy_path.csv")

        # when
        actual = loader.get_data_between(start_time, end_time)

        # then
        self.assertEqual(actual, expected)  # Should return an empty list for an empty file

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="time,meterusage\n2023-01-01 10:00:00,100\n2023-01-01 11:00:00,NaN\n"
    )
    def test_NaN_meterusage_field(self, mock_file):
        # given
        start_time = datetime(2023, 1, 1, 9, 0, tzinfo=timezone.utc)
        end_time = datetime(2023, 1, 1, 12, 0, tzinfo=timezone.utc)
        expected = [
            DataPoint(datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc), 100.0),
        ]
        loader = CSVDataLoader("dummy_path.csv")

        # when
        actual = loader.get_data_between(start_time, end_time)

        # then
        self.assertEqual(actual, expected)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="time,meterusage\n2023-01-01 10:00:00,100\ninvalid_date,50\n"
    )
    def test_invalid_date_format(self, mock_file):
        # given
        start_time = datetime(2023, 1, 1, 9, 0, tzinfo=timezone.utc)
        end_time = datetime(2023, 1, 1, 12, 0, tzinfo=timezone.utc)
        loader = CSVDataLoader("dummy_path.csv")

        # when & then
        with self.assertRaises(ValueError):
            loader.get_data_between(start_time, end_time)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="time,meterusage\n2023-01-01 10:00:00,100\n2023-01-01 11:00:00,200\n2023-01-01 12:00:00,300"
    )
    def test_multi_data_points(self, mock_file):
        # given
        start_time = datetime(2023, 1, 1, 9, 0, 0, tzinfo=timezone.utc)
        end_time = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        expected = [
            DataPoint(datetime(2023, 1, 1, 10, 0, 0, tzinfo=timezone.utc), 100.0),
            DataPoint(datetime(2023, 1, 1, 11, 0, 0, tzinfo=timezone.utc), 200.0)
        ]
        loader = CSVDataLoader("dummy_path.csv")

        # when
        actual = loader.get_data_between(start_time, end_time)

        # then
        self.assertEqual(actual, expected)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="time,meterusage\n2023-01-01 10:00:00,100\n2023-01-01 11:00:00,200\n2023-01-01 12:00:00,300"
    )
    def test_start_time_timezone(self, mock_file):
        # given
        start_time = datetime(2023, 1, 1,10, tzinfo=timezone.min)
        end_time = datetime(2023, 1, 1, 11, tzinfo=timezone.min)
        expected = [
            DataPoint(datetime(2023, 1, 1, 11, tzinfo=timezone.utc), 200.0)
        ]
        loader = CSVDataLoader("dummy_path.csv")

        # when
        actual = loader.get_data_between(start_time, end_time)

        # then
        self.assertNotEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
