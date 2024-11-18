import unittest
from unittest.mock import MagicMock
from datetime import datetime, timezone
import grpc
from src.server.proto import metric_service_pb2
from src.server.server import MetricService
from src.domain.metric.data_point import DataPoint
from src.domain.metric.metric_use_case import MetricUseCase


class TestMetricService(unittest.TestCase):

    def test_metric_service_get_data(self):
        # given
        start_time = datetime(2023, 1, 2)
        end_time = datetime(2023, 1, 1)

        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)

        metric_use_case_mock = MagicMock(spec=MetricUseCase)
        metric_use_case_mock.get_data_between.return_value = [
            DataPoint(datetime(2023, 1, 3), 100.0)
        ]
        metric_service = MetricService(metric_use_case_mock)
        mock_context = MagicMock()

        # when
        response = metric_service.GetMetrics(request, mock_context)

        # then
        metric_use_case_mock.get_data_between.assert_called_with(
            datetime(2023, 1, 2, tzinfo=timezone.utc),
            datetime(2023, 1, 1, tzinfo=timezone.utc)
        )
        self.assertEqual(len(response.data_points), 1)
        self.assertEqual(response.data_points[0].value, 100.0)

    def test_empty_data_points(self):
        #given
        start_time = datetime(2023, 1, 2)
        end_time = datetime(2023, 1, 1)

        metric_use_case_mock = MagicMock(spec=MetricUseCase)
        metric_use_case_mock.get_data_between.return_value = []

        metric_service = MetricService(metric_use_case_mock)

        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)
        mock_context = MagicMock()
        
        #when
        response = metric_service.GetMetrics(request, mock_context)

        #then
        self.assertEqual(len(response.data_points), 0)

    def test_check_error(self):
        # given
        start_time = datetime(2023, 1, 2)
        end_time = datetime(2023, 1, 1)

        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)

        metric_use_case_mock = MagicMock(spec=MetricUseCase)
        metric_use_case_mock.get_data_between.side_effect = ValueError("Test error")

        metric_service = MetricService(metric_use_case_mock)

        mock_context = MagicMock()

        # when
        response = metric_service.GetMetrics(request, mock_context)

        # then
        mock_context.set_code.assert_called_once_with(grpc.StatusCode.INTERNAL)
        mock_context.set_details.assert_called_once_with("An internal error occurred: Test error")
        self.assertIsInstance(response, metric_service_pb2.MetricResponse)



if __name__ == '__main__':
    unittest.main()
