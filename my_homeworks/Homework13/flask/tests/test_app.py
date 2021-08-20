import pytest
from tests.conftest import client, ApiMock
from config import Config


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "b1c4d66426msh184569cb345602cp118396jsn61e44b74223b"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"cities": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


def test_search_weather_v2(client, mocker, fake_weather_api=ApiMock):
    fake_weather_api = fake_weather_api()
    mocker.patch('requests.request', return_value=fake_weather_api)
    response = client.post("/search", data={"cities": "Lisbon"})
    assert response.status_code == 200
    assert b"Weather for Lisbon" in response.data
