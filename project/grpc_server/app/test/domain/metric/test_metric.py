import unittest
from unittest.mock import MagicMock
from datetime import datetime
from domain.metric.data_point import DataPoint
from domain.data_loader.base import DataLoader
from domain.metric.metric_use_case import MetricUseCase


class TestMetric(unittest.TestCase):

    def _get_fake_metric_use_case(self, loader_mock):
        return MetricUseCase(data_loader=loader_mock)

    def test_multiple_data_points(self):
        # given
        start_time = datetime(2023, 1, 1, 9, 0)
        end_time = datetime(2023, 1, 1, 12, 0)
        expected = [
            DataPoint(datetime(2023, 1, 1, 10, 0, 0), 100.0),
            DataPoint(datetime(2023, 1, 1, 11, 0, 0), 200.0)
        ]

        # Create a mock DataLoader
        loader_mock = MagicMock(spec=DataLoader)
        loader_mock.get_data_between.return_value = expected  # Simulate return value

        # Create the Metric object with the mock loader
        metric_use_case = self._get_fake_metric_use_case(loader_mock)

        # when
        actual = metric_use_case.get_data_between(start_time, end_time)

        # then
        self.assertEqual(actual, expected)
        loader_mock.get_data_between.assert_called_once_with(start_time, end_time)

    def test_no_data_points(self):
        # given
        start_time = datetime(2023, 1, 1)
        end_time = datetime(2023, 1, 2)
        expected = []  # No data points for the given range

        # Create a mock DataLoader
        loader_mock = MagicMock(spec=DataLoader)
        loader_mock.get_data_between.return_value = expected  # Simulate no data points

        # Create the Metric object with the mock loader
        metric_use_case = self._get_fake_metric_use_case(loader_mock)

        # when
        actual = metric_use_case.get_data_between(start_time, end_time)

        # then
        self.assertEqual(actual, expected)  # Should return an empty list
        loader_mock.get_data_between.assert_called_once_with(start_time, end_time)


    def test_invalid_data_points(self):
        # given
        start_time = datetime(2023, 1, 1)
        end_time = datetime(2023, 1, 2)

        # Simulate invalid data points, e.g., NaN or None values
        expected = [
            DataPoint(datetime(2023, 1, 1, 10, 0, 0), float('nan')),  # Invalid data (NaN)
            DataPoint(datetime(2023, 1, 1, 11, 0, 0), None)  # Invalid data (None)
        ]

        # Create a mock DataLoader
        loader_mock = MagicMock(spec=DataLoader)
        loader_mock.get_data_between.return_value = expected  # Simulate invalid data points

        # Create the Metric object with the mock loader
        metric_use_case = self._get_fake_metric_use_case(loader_mock)

        # when
        actual = metric_use_case.get_data_between(start_time, end_time)

        # then
        self.assertEqual(actual, expected)
        # Verify that get_data_between was called once with correct arguments
        loader_mock.get_data_between.assert_called_once_with(start_time, end_time)


if __name__ == "__main__":
    unittest.main()
