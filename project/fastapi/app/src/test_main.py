from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_general():
    response = client.get("/get_consumptions?start_time=2019-01-01%2001%3A00%3A00&end_time=2019-01-01%2001%3A30%3A00")
    assert response.status_code == 200
    assert response.json() == {
                "data_points": [
                    {
                    "value": 56.03,
                    "time": "2019-01-01T01:00:00"
                    },
                    {
                    "value": 55.77,
                    "time": "2019-01-01T01:15:00"
                    }
                ]
            }