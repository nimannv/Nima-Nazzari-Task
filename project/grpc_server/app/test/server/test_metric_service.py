import unittest
from unittest.mock import MagicMock
from datetime import datetime, timezone
import grpc
from server.proto import metric_service_pb2
from server.server import MetricService
from domain.metric.data_point import DataPoint
from domain.metric.metric_use_case import MetricUseCase


class TestMetricService(unittest.TestCase):

    def test_metric_service_get_data(self):
        """
        Test that MetricService correctly calls the Metric get_data_between method without checking time.
        """
        # given
        start_time = datetime(2023, 1, 2)
        end_time = datetime(2023, 1, 1)

        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)

        metric_use_case_mock = MagicMock(spec=MetricUseCase)
        metric_use_case_mock.get_data_between.return_value = [
            DataPoint(datetime(2023, 1, 3), 100.0)
        ]
        metric_service = MetricService(metric_use_case_mock)

        # when
        response = metric_service.GetMetrics(request, None)

        # then
        metric_use_case_mock.get_data_between.assert_called_with(
            datetime(2023, 1, 2, tzinfo=timezone.utc),
            datetime(2023, 1, 1, tzinfo=timezone.utc)
        )
        self.assertEqual(len(response.data_points), 1)
        self.assertEqual(response.data_points[0].value, 100.0)

    def test_empty_data_points(self):
        """
        Test when the query returns no data points within the given time range.
        """
        #given
        start_time = datetime(2023, 1, 2)
        end_time = datetime(2023, 1, 1)

        metric_use_case_mock = MagicMock(spec=MetricUseCase)
        metric_use_case_mock.get_data_between.return_value = []

        metric_service = MetricService(metric_use_case_mock)

        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)
        
        #when
        response = metric_service.GetMetrics(request, None)

        #then
        self.assertEqual(len(response.data_points), 0)

    def test_check_error(self):
        # given
        start_time = datetime(2023, 1, 2)
        end_time = datetime(2023, 1, 1)

        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)

        metric_use_case_mock = MagicMock(spec=MetricUseCase)
        metric_use_case_mock.get_data_between.side_effect = ValueError

        metric_sevice = MetricService(metric_use_case_mock)

        # then
        with self.assertRaises(ValueError):
            metric_sevice.GetMetrics(request, None)



if __name__ == '__main__':
    unittest.main()
