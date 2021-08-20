from tests.conftest import client, todos
import json
from config import Config


def test_create(client, todos):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/todos", headers=headers, json=todos)
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_list(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_update(client):
    update_data = {
        "text": "blablabla"
    }

    response = client.put("/todos/1", json=update_data)
    assert response.status_code == 200
    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json['1'] == "blablabla"


def test_delete(client):
    response = client.delete("/todos/1")
    assert response.status_code == 204
    response = client.get("/todos/1")
    assert response.status_code == 404


class FakeDataMock:
    def __init__(self):
        self.api_data = {
                    "id": 702550,
                    "name": "Lviv",
                    "coord": {
                        "lat": 49.8383,
                        "lon": 24.0232
                    },
                    "main": {
                        "temp": 23,
                        "feels_like": 22.82,
                        "temp_min": 23,
                        "temp_max": 23,
                        "pressure": 1020,
                        "humidity": 56
                    },
                    "dt": 1624043349,
                    "wind": {
                        "speed": 3,
                        "deg": 100
                    },
                    "sys": {
                        "country": "UA"
                    },
                    "rain": None,
                    "snow": None,
                    "clouds": {
                        "all": 0
                    },
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01n"
                        }
                    ]
                }

        self.status_code = 200

    def json(self):
        return self.api_data


def test_weather(client, mocker, fake_data=FakeDataMock()):
    Config.WEATHER_API_KEY = "b1c4d66426msh184569cb345602cp118396jsn61e44b74223b"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    # mocker.patch('requests.request', url="https://community-open-weather-map.p.rapidapi.com/find",
    #              return_value=fake_data)
    response = client.get('/weather?city=Lviv,London')
    assert response.status_code == 200
    assert response.json[0][0]['name'] == 'Lviv'
    assert response.json[1][0]['name'] == 'London'
